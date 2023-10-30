# Generated by Django 4.2.6 on 2023-10-30 04:46

import account.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(help_text='ضروری', max_length=50, verbose_name='نام شرکت')),
                ('national_code', models.CharField(help_text='ضروری', max_length=10, validators=[account.validators.validate_national_code], verbose_name='کد ملی')),
                ('address', models.TextField(help_text='ضروری', max_length=200, verbose_name='آدرس')),
                ('landline_phone', models.CharField(help_text='ضروری', max_length=15, validators=[account.validators.validate_landline_phone], verbose_name='شماره تلفن ثابت')),
                ('mobile_phone', models.CharField(help_text='ضروری', max_length=11, validators=[account.validators.validate_mobile_phone], verbose_name='شماره تلفن همراه')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, validators=[account.validators.validate_email], verbose_name='آدرس ایمیل')),
                ('request_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ درخواست')),
                ('instance_sent_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ارسال نمونه')),
                ('test_name', models.CharField(help_text='ضروری', max_length=100, verbose_name='نام آزمون')),
                ('instance_details', models.TextField(help_text='ضروری', max_length=2000, verbose_name='مشخصات نمونه')),
                ('description', models.TextField(help_text='ضروری', max_length=2000, verbose_name='توضیحات')),
            ],
            options={
                'verbose_name': 'فرم پذیرش',
                'verbose_name_plural': 'فرم های پذیرش',
            },
        ),
    ]