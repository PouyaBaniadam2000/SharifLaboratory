from django.db import models

from account.models import CustomUser


class Message(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان", help_text="ضروری")
    name = models.CharField(max_length=100, verbose_name="نام و نام خانوادگی", help_text="ضروری")
    mobile_phone = models.CharField(max_length=11, verbose_name="شماره تلفن همراه", help_text="ضروری")
    email = models.EmailField(max_length=255, verbose_name="آدرس ایمیل", help_text="ضروری")
    body = models.TextField(max_length=1000, verbose_name="بدنه", help_text="ضروری")

    def __str__(self):
        return f"{self.title} - {self.name}"

    class Meta:
        verbose_name = "پیام"
        verbose_name_plural = "پیام ها"


class Complaint(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="کاربر", help_text="ضروری")
    body = models.TextField(max_length=500, verbose_name="بدنه", help_text="ضروری")

    def __str__(self):
        return "شکایت"

    class Meta:
        verbose_name = "شکایت"
        verbose_name_plural = "شکایات"


class ContactInfo(models.Model):
    work_time = models.CharField(max_length=200, verbose_name="ساعت کاری", help_text="ضروری")
    address = models.CharField(max_length=200, verbose_name="آدرس", help_text="ضروری")
    email = models.EmailField(max_length=255, verbose_name="ایمیل", help_text="ضروری")
    mobile_phone = models.CharField(max_length=11, verbose_name="شماره تلفن همراه", help_text="ضروری")
    landline_phone = models.CharField(unique=True, max_length=15, verbose_name="شماره تلفن ثابت", help_text="ضروری")

    def __str__(self):
        return "پل ارتباطی"

    class Meta:
        verbose_name = "پل ارتباطی"
        verbose_name_plural = "پل های ارتباطی"
