from django.db import models

from account.validators import validate_landline_phone, validate_email, validate_mobile_phone, validate_national_code


class Admission(models.Model):
    company_name = models.CharField(max_length=50, verbose_name="نام شرکت", help_text="ضروری")
    national_code = models.CharField(max_length=10, verbose_name="کد ملی", help_text="ضروری",
                                     validators=[validate_national_code])
    address = models.TextField(max_length=200, verbose_name="آدرس", help_text="ضروری")
    landline_phone = models.CharField(max_length=15, verbose_name="شماره تلفن ثابت",
                                      validators=[validate_landline_phone], help_text="ضروری")
    mobile_phone = models.CharField(max_length=11, help_text="ضروری", verbose_name="شماره تلفن همراه",
                                    validators=[validate_mobile_phone])
    email = models.EmailField(verbose_name="آدرس ایمیل",
                              validators=[validate_email])
    request_date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ درخواست")
    instance_sent_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="تاریخ ارسال نمونه")
    test_name = models.CharField(max_length=100, verbose_name="نام آزمون", help_text="ضروری")
    instance_details = models.TextField(max_length=2000, verbose_name="مشخصات نمونه", help_text="ضروری")
    description = models.TextField(max_length=2000, verbose_name="توضیحات", help_text="ضروری")

    class Meta:
        verbose_name = "فرم پذیرش"
        verbose_name_plural = "فرم های پذیرش"

    def __str__(self):
        return "فرم پذیرش"
