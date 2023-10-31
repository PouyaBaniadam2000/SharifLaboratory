from django.utils.text import slugify

from account.validators import validate_mobile_phone, validate_username, validate_first_name, validate_email, \
    validate_last_name, validate_landline_phone
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import validate_slug
from django.db import models
from django.templatetags.static import static
from django.utils.html import format_html


class CustomUserManager(BaseUserManager):
    def create_user(self, mobile_phone, username=None, email=None, password=None, **extra_fields):
        if not mobile_phone:
            raise ValueError('کاربر باید شماره تلفن داشته باشد.')

        if not username:
            raise ValueError('کاربر باید نام کاربری داشته باشد.')

        user = self.model(
            mobile_phone=self.normalize_phone(mobile_phone),
            username=username,
            email=self.normalize_email(email) if email else None,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, mobile_phone, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('کارمند باید مقدار is_staff=True را داشته باشد.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('ابر کاربر باید مقدار is_staff=True را داشته باشد.')

        return self.create_user(mobile_phone, username, email, password, **extra_fields)

    def normalize_phone(self, mobile_phone):
        return ''.join(filter(str.isdigit, mobile_phone))


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=50, help_text="ضروری", verbose_name="نام کاربری",
                                validators=[validate_username])

    mobile_phone = models.CharField(unique=True, max_length=11, help_text="ضروری", verbose_name="شماره تلفن همراه",
                                    validators=[validate_mobile_phone], blank=False, null=False)

    landline_phone = models.CharField(unique=True, max_length=15, help_text="ضروری", verbose_name="شماره تلفن ثابت",
                                      validators=[validate_landline_phone], blank=False, null=False)

    postal_code = models.CharField(unique=True, max_length=20, help_text="ضروری", verbose_name="کد پستی", blank=False,
                                   null=False)

    address = models.TextField(unique=True, max_length=200, help_text="ضروری", verbose_name="آدرس", blank=False,
                               null=False)

    company_name = models.CharField(max_length=100, help_text="ضروری", verbose_name="نام شرکت", blank=False, null=False)

    activity_field = models.CharField(max_length=100, verbose_name="حوزه فعالیت", blank=True, null=True)

    email = models.EmailField(unique=True, blank=True, null=True, verbose_name="آدرس ایمیل",
                              validators=[validate_email], help_text="ضروری")

    first_name = models.CharField(max_length=50, blank=False, null=False, verbose_name="نام",
                                  validators=[validate_first_name], help_text="ضروری")

    last_name = models.CharField(max_length=50, blank=False, null=False, verbose_name="نام خانوادگی",
                                 validators=[validate_last_name], help_text="ضروری")

    image = models.ImageField(upload_to='account/custom user/images', blank=True, null=True,
                              verbose_name="تصویر پروفایل")

    slug = models.SlugField(editable=False, unique=True, blank=True, null=True, verbose_name="اسلاگ",
                            validators=[validate_slug], help_text="ضروری")

    is_staff = models.BooleanField(default=False, verbose_name="کارمند")

    is_active = models.BooleanField(default=True, verbose_name="فعال")

    date_joined = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="تاریخ پیوستن")

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['mobile_phone']

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        self.username = self.username.lower()

        super().save(*args, **kwargs)

    def show_image(self):
        if self.image:
            return format_html(
                f'<a href="{self.image.url}"><img style="border-radius: 100%" src="{self.image.url}" alt="{self.image.name}" width="30px" height="30px"></a>')
        else:
            return format_html(
                '<img src="{}" style="width: 30px; height: 30px;">'.format(
                    static("assets/images/profile.png")))

    def __str__(self):
        return self.username


class OTP(models.Model):
    username = models.CharField(max_length=50, blank=True, null=True, verbose_name="نام کاربری", default="")
    mobile_phone = models.CharField(max_length=11, verbose_name="شماره تلفن همراه")
    landline_phone = models.CharField(max_length=15, verbose_name="شماره تلفن ثابت")
    postal_code = models.CharField(max_length=20, verbose_name="کد پستی")
    address = models.CharField(max_length=200, verbose_name="آدرس")
    company_name = models.CharField(max_length=100, verbose_name="نام شرکت")
    activity_field = models.CharField(max_length=100, verbose_name="حوزه فعالیت", blank=True, null=True)
    email = models.CharField(max_length=255, verbose_name="آدرس ایمیل")
    first_name = models.CharField(max_length=50, verbose_name="نام")
    last_name = models.CharField(max_length=50, verbose_name="نام خانوادگی")
    password = models.CharField(max_length=100, editable=False, blank=True, null=True, verbose_name="رمز عبور",
                                default="")
    code = models.CharField(max_length=5, verbose_name="کد")
    token = models.CharField(max_length=36, verbose_name="توکن")
    type = models.CharField(max_length=50, verbose_name="نوع")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="ایجاد شده در تاریخ")
    delete_at = models.DateTimeField(null=True, blank=True, verbose_name="حذف شده در تاریخ")

    class Meta:
        verbose_name = "اُ-تی-پی"
        verbose_name_plural = "اُ-تی-پی ها"

    def __str__(self):
        return f"{self.mobile_phone}"

    def delete(self, *args, **kwargs):
        super(OTP, self).delete(*args, **kwargs)