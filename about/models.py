from django.db import models


class About(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name="تیتر", help_text="ضروری")
    body = models.TextField(max_length=500, unique=True, verbose_name="بدنه", help_text="ضروری")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "درباره"
        verbose_name_plural = "درباره ها"


class Faq(models.Model):
    question = models.CharField(max_length=500, verbose_name="سوال", unique=True, help_text="ضروری")
    answer = models.TextField(max_length=1500, verbose_name="پاسخ", unique=True, help_text="ضروری")

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "سوال متداول"
        verbose_name_plural = "سوالات متداول"
