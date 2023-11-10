from django.db import models
from ckeditor.fields import RichTextField
from django.utils.html import format_html


class Category(models.Model):
    parent = models.ForeignKey("self", blank=True, null=True, on_delete=models.CASCADE, verbose_name="والد",
                               help_text="ضروری", related_name="subs")
    title = models.CharField(max_length=100, verbose_name="تیتر", help_text="ضروری")
    slug = models.SlugField(allow_unicode=True, max_length=150, verbose_name="اسلاگ (متن داخل URL)", help_text="ضروری")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"


class Laboratory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="دسته بندی", help_text="ضروری")
    title = models.CharField(max_length=50, verbose_name="تیتر", help_text="ضروری")
    laboratory_preview = models.CharField(max_length=200, verbose_name="درباره آزمایشگاه", help_text="ضروری")
    image_1 = models.ImageField(upload_to="laboratory/laboratory/images", verbose_name="تصویر 1", help_text="ضروری")
    image_2 = models.ImageField(upload_to="laboratory/laboratory/images", verbose_name="تصویر 2", help_text="ضروری")
    image_3 = models.ImageField(upload_to="laboratory/laboratory/images", verbose_name="تصویر 3", help_text="ضروری")
    image_4 = models.ImageField(upload_to="laboratory/laboratory/images", verbose_name="تصویر 4", help_text="ضروری")
    image_5 = models.ImageField(upload_to="laboratory/laboratory/images", verbose_name="تصویر 5", blank=True, null=True)
    image_6 = models.ImageField(upload_to="laboratory/laboratory/images", verbose_name="تصویر 6", blank=True, null=True)
    body = RichTextField(max_length=50000, verbose_name="بدنه", unique=True, help_text="ضروری")
    is_allowed = models.BooleanField(default=True, verbose_name="مجوز نشان داده شدن دارد؟")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="ایجاد شده در تاریخ")
    slug = models.SlugField(unique=True, allow_unicode=True, blank=True, null=True, verbose_name="اسلاگ (متن داخل URL)")

    def __str__(self):
        return self.title

    def show_image_1(self):
        return format_html(
            f'<a href="{self.image_1.url}"><img style="border-radius: 100%" src="{self.image_1.url}" alt="{self.image_1.name}" width="30px" height="30px"></a>')

    def show_image_2(self):
        return format_html(
            f'<a href="{self.image_2.url}"><img style="border-radius: 100%" src="{self.image_2.url}" alt="{self.image_2.name}" width="30px" height="30px"></a>')

    def show_image_3(self):
        return format_html(
            f'<a href="{self.image_3.url}"><img style="border-radius: 100%" src="{self.image_3.url}" alt="{self.image_3.name}" width="30px" height="30px"></a>')

    def show_image_4(self):
        return format_html(
            f'<a href="{self.image_4.url}"><img style="border-radius: 100%" src="{self.image_4.url}" alt="{self.image_4.name}" width="30px" height="30px"></a>')

    class Meta:
        verbose_name = "آزمایشگاه"
        verbose_name_plural = "آزمایشگاه ها"
        ordering = ("-created_at",)
