from account.models import CustomUser
from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField


class Weblog(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="نویسنده", related_name="weblogs",
                               help_text="ضروری")
    title = models.CharField(max_length=50, verbose_name="تیتر", help_text="ضروری")
    weblog_preview = models.CharField(max_length=200, verbose_name="درباره مقاله", help_text="ضروری")
    image = models.ImageField(upload_to="weblog/weblog/images", verbose_name="تصویر", help_text="ضروری")
    body = RichTextField(max_length=50000, verbose_name="بدنه", unique=True, help_text="ضروری")
    categories = models.ManyToManyField("Category", related_name='weblogs', verbose_name="کتگوری ها", help_text="ضروری")
    is_allowed = models.BooleanField(default=True, verbose_name="مجوز نشان داده شدن دارد؟", help_text="ضروری")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="ایجاد شده در تاریخ")
    actual_jalali_date = models.CharField(max_length=100, blank=True, null=True, verbose_name="تاریخ جلالی",
                                          help_text="ضروری")
    slug = models.SlugField(unique=True, allow_unicode=True, blank=True, null=True, verbose_name="اسلاگ (متن داخل URL)")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "وبلاگ"
        verbose_name_plural = "وبلاگ ها"
        ordering = ("-created_at",)


class Category(models.Model):
    category = models.CharField(max_length=100, verbose_name="کتگوری", help_text="ضروری")
    is_allowed = models.BooleanField(default=True, verbose_name="مجوز نشان داده شدن دارد؟")

    class Meta:
        verbose_name = "کتگوری"
        verbose_name_plural = "کتگوری ها"

    def __str__(self):
        return self.category
