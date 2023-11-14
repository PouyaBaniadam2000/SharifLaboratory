from ckeditor.fields import RichTextField
from django.db import models
from django.utils.html import format_html


class Record(models.Model):
    title = models.CharField(max_length=50, verbose_name="تیتر", help_text="ضروری")
    record_preview = models.CharField(max_length=200, verbose_name="درباره سابقه", help_text="ضروری")
    image_1 = models.ImageField(upload_to="new/new/images", verbose_name="تصویر 1", help_text="ضروری")
    image_2 = models.ImageField(upload_to="new/new/images", verbose_name="تصویر 2", blank=True, null=True)
    image_3 = models.ImageField(upload_to="new/new/images", verbose_name="تصویر 3", blank=True, null=True)
    image_4 = models.ImageField(upload_to="new/new/images", verbose_name="تصویر 4", blank=True, null=True)
    image_5 = models.ImageField(upload_to="new/new/images", verbose_name="تصویر 5", blank=True, null=True)
    image_6 = models.ImageField(upload_to="new/new/images", verbose_name="تصویر 6", blank=True, null=True)
    image_7 = models.ImageField(upload_to="new/new/images", verbose_name="تصویر 7", blank=True, null=True)
    image_8 = models.ImageField(upload_to="new/new/images", verbose_name="تصویر 8", blank=True, null=True)

    body = RichTextField(max_length=50000, verbose_name="بدنه", unique=True, help_text="ضروری")
    categories = models.ManyToManyField("Category", related_name='weblogs', verbose_name="کتگوری ها", help_text="ضروری")
    is_allowed = models.BooleanField(default=True, verbose_name="مجوز نشان داده شدن دارد؟")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="ایجاد شده در تاریخ")
    slug = models.SlugField(unique=True, allow_unicode=True, blank=True, null=True, verbose_name="اسلاگ (متن داخل URL)")

    def __str__(self):
        return self.title

    def show_image(self):
        return format_html(
            f'<a href="{self.image_1.url}"><img style="border-radius: 100%" src="{self.image_1.url}" alt="{self.image_1.name}" width="30px" height="30px"></a>')

    class Meta:
        verbose_name = "سابقه"
        verbose_name_plural = "سوابق"
        ordering = ("-created_at",)


class Category(models.Model):
    category = models.CharField(max_length=100, verbose_name="کتگوری", help_text="ضروری")
    is_allowed = models.BooleanField(default=True, verbose_name="مجوز نشان داده شدن دارد؟")

    class Meta:
        verbose_name = "کتگوری"
        verbose_name_plural = "کتگوری ها"

    def __str__(self):
        return self.category
