# Generated by Django 4.2.6 on 2023-10-31 06:19

import account.validators
import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='نام کاربری')),
                ('mobile_phone', models.CharField(max_length=11, verbose_name='شماره تلفن همراه')),
                ('landline_phone', models.CharField(max_length=15, verbose_name='شماره تلفن ثابت')),
                ('postal_code', models.CharField(max_length=20, verbose_name='کد پستی')),
                ('address', models.CharField(max_length=200, verbose_name='آدرس')),
                ('company_name', models.CharField(max_length=100, verbose_name='نام شرکت')),
                ('activity_field', models.CharField(blank=True, max_length=100, null=True, verbose_name='حوزه فعالیت')),
                ('email', models.CharField(max_length=255, verbose_name='آدرس ایمیل')),
                ('first_name', models.CharField(max_length=50, verbose_name='نام')),
                ('last_name', models.CharField(max_length=50, verbose_name='نام خانوادگی')),
                ('password', models.CharField(blank=True, default='', editable=False, max_length=100, null=True, verbose_name='رمز عبور')),
                ('code', models.CharField(max_length=5, verbose_name='کد')),
                ('token', models.CharField(max_length=36, verbose_name='توکن')),
                ('type', models.CharField(max_length=50, verbose_name='نوع')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='ایجاد شده در تاریخ')),
                ('delete_at', models.DateTimeField(blank=True, null=True, verbose_name='حذف شده در تاریخ')),
            ],
            options={
                'verbose_name': 'اُ-تی-پی',
                'verbose_name_plural': 'اُ-تی-پی ها',
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(help_text='ضروری', max_length=50, unique=True, validators=[account.validators.validate_username], verbose_name='نام کاربری')),
                ('mobile_phone', models.CharField(help_text='ضروری', max_length=11, unique=True, validators=[account.validators.validate_mobile_phone], verbose_name='شماره تلفن همراه')),
                ('landline_phone', models.CharField(help_text='ضروری', max_length=15, unique=True, validators=[account.validators.validate_landline_phone], verbose_name='شماره تلفن ثابت')),
                ('postal_code', models.CharField(help_text='ضروری', max_length=20, unique=True, verbose_name='کد پستی')),
                ('address', models.TextField(help_text='ضروری', max_length=200, unique=True, verbose_name='آدرس')),
                ('company_name', models.CharField(help_text='ضروری', max_length=100, verbose_name='نام شرکت')),
                ('activity_field', models.CharField(blank=True, max_length=100, null=True, verbose_name='حوزه فعالیت')),
                ('email', models.EmailField(blank=True, help_text='ضروری', max_length=254, null=True, unique=True, validators=[account.validators.validate_email], verbose_name='آدرس ایمیل')),
                ('first_name', models.CharField(help_text='ضروری', max_length=50, validators=[account.validators.validate_first_name], verbose_name='نام')),
                ('last_name', models.CharField(help_text='ضروری', max_length=50, validators=[account.validators.validate_last_name], verbose_name='نام خانوادگی')),
                ('image', models.ImageField(blank=True, null=True, upload_to='account/custom user/images', verbose_name='تصویر پروفایل')),
                ('slug', models.SlugField(blank=True, editable=False, help_text='ضروری', null=True, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), 'Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.', 'invalid')], verbose_name='اسلاگ')),
                ('is_staff', models.BooleanField(default=False, verbose_name='کارمند')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ پیوستن')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'کاربران',
            },
        ),
    ]
