from django.db import models
from ckeditor.fields import RichTextField
from django.utils.html import format_html
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام")
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, verbose_name="والد")

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def __str__(self):
        return self.name


class Laboratory(models.Model):
    title = models.CharField(max_length=50, verbose_name="تیتر", help_text="ضروری")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="دسته‌بندی محصول")
    record_preview = models.CharField(max_length=200, verbose_name="درباره سابقه", help_text="ضروری")
    image_1 = models.ImageField(upload_to="laboratory/laboratory/images", verbose_name="تصویر 1", help_text="ضروری")
    image_2 = models.ImageField(upload_to="laboratory/laboratory/images", verbose_name="تصویر 2", help_text="ضروری")
    image_3 = models.ImageField(upload_to="laboratory/laboratory/images", verbose_name="تصویر 3", help_text="ضروری")
    image_4 = models.ImageField(upload_to="laboratory/laboratory/images", verbose_name="تصویر 4", help_text="ضروری")
    image_5 = models.ImageField(upload_to="laboratory/laboratory/images", verbose_name="تصویر 5", blank=True, null=True)
    image_6 = models.ImageField(upload_to="laboratory/laboratory/images", verbose_name="تصویر 6", blank=True, null=True)
    image_7 = models.ImageField(upload_to="laboratory/laboratory/images", verbose_name="تصویر 7", blank=True, null=True)
    image_8 = models.ImageField(upload_to="laboratory/laboratory/images", verbose_name="تصویر 8", blank=True, null=True)
    body = RichTextField(max_length=50000, verbose_name="بدنه", unique=True, help_text="ضروری")
    location = models.CharField(max_length=100, verbose_name="لوکیشن", help_text="ضروری")
    financial_value = models.CharField(max_length=50, verbose_name="ارزش مالی", help_text="ضروری")
    date = models.CharField(max_length=100, verbose_name="تاریخ ساخت سابقه", help_text="ضروری")
    is_allowed = models.BooleanField(default=True, verbose_name="مجوز نشان داده شدن دارد؟")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="ایجاد شده در تاریخ")
    slug = models.SlugField(unique=True, allow_unicode=True, blank=True, null=True, verbose_name="اسلاگ (متن داخل URL)")

    def __str__(self):
        return self.title

    def show_image(self):
        return format_html(
            f'<a href="{self.image_1.url}"><img style="border-radius: 100%" src="{self.image_1.url}" alt="{self.image_1.name}" width="30px" height="30px"></a>')

    class Meta:
        verbose_name = "آزمایشگاه"
        verbose_name_plural = "آزمایشگاه ها"
        ordering = ("-created_at",)
