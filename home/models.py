from django.conf.urls.static import static
from django.db import models
from django.utils.html import format_html


class GeneralWebsiteIdea(models.Model):
    title = models.CharField(max_length=50, verbose_name="تیتر", help_text="ضروری")
    body = models.TextField(max_length=500, verbose_name="بدنه", help_text="ضروری")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "ایده کلی"
        verbose_name_plural = "ایده های کلی"


class GeneralWebsiteIdeaImage(models.Model):
    image = models.ImageField(upload_to="home/general website idea image/images", verbose_name="تصویر",
                              help_text="ضروری")

    def __str__(self):
        return "تصویر"

    def show_image(self):
        if self.image:
            return format_html(
                f'<a href="{self.image.url}"><img style="border-radius: 100%" src="{self.image.url}" alt="{self.image.name}" width="30px" height="30px"></a>')
        else:
            return format_html(
                '<img src="{}" style="width: 30px; height: 30px;">'.format(
                    static("assets/images/profile.png")))

    class Meta:
        verbose_name = "تصویر ایده کلی سایت"
        verbose_name_plural = "تصاویر ایده کلی سایت"


class SharifLabServicePreview(models.Model):
    icon = models.ImageField(upload_to="home/sharif lab service preview/images", verbose_name="آیکون",
                             help_text="ضروری")
    title = models.CharField(max_length=50, verbose_name="تیتر", help_text="ضروری")
    body = models.TextField(max_length=500, verbose_name="بدنه", help_text="ضروری")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "پری ویو خدمت آزمایشگاه شریف"
        verbose_name_plural = "پری ویو های خدمات آزمایشگاه شریف"


class TeamMember(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="نام و نام خانوادگی", help_text="ضروری")
    role = models.CharField(max_length=100, unique=True, verbose_name="نقش", help_text="ضروری")
    about = models.TextField(max_length=1000, unique=True, verbose_name="درباره", help_text="ضروری")
    image = models.ImageField(upload_to="home/team member/images", verbose_name="تصویر", help_text="ضروری")

    def __str__(self):
        return self.name

    def show_image(self):
        if self.image:
            return format_html(
                f'<a href="{self.image.url}"><img style="border-radius: 100%" src="{self.image.url}" alt="{self.image.name}" width="30px" height="30px"></a>')
        else:
            return format_html(
                '<img src="{}" style="width: 30px; height: 30px;">'.format(
                    static("assets/images/profile.png")))

    class Meta:
        verbose_name = "عضو تیم"
        verbose_name_plural = "اعضای تیم"


class Certificate(models.Model):
    title = models.CharField(max_length=50, verbose_name="گواهینامه", help_text="ضروری")
    image = models.ImageField(upload_to="home/Certificate/images", verbose_name="تصویر", help_text="ضروری")
    is_allowed = models.BooleanField(default=True, verbose_name="مجوز نشان داده شدن دارد؟")

    def __str__(self):
        return self.title

    def show_image(self):
        if self.image:
            return format_html(
                f'<a href="{self.image.url}"><img style="border-radius: 100%" src="{self.image.url}" alt="{self.image.name}" width="30px" height="30px"></a>')
        else:
            return format_html(
                '<img src="{}" style="width: 30px; height: 30px;">'.format(
                    static("assets/images/profile.png")))

    class Meta:
        verbose_name = "گواهینامه"
        verbose_name_plural = "گواهینامه ها"
