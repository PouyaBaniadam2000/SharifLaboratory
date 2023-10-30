# Generated by Django 4.2.6 on 2023-10-30 04:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(help_text='ضروری', max_length=200, verbose_name='آدرس')),
                ('email', models.EmailField(help_text='ضروری', max_length=255, verbose_name='ایمیل')),
                ('mobile_phone', models.CharField(help_text='ضروری', max_length=11, verbose_name='شماره تلفن همراه')),
                ('landline_phone', models.CharField(help_text='ضروری', max_length=15, unique=True, verbose_name='شماره تلفن ثابت')),
            ],
            options={
                'verbose_name': 'پل ارتباطی',
                'verbose_name_plural': 'پل های ارتباطی',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='ضروری', max_length=100, verbose_name='عنوان')),
                ('name', models.CharField(help_text='ضروری', max_length=100, verbose_name='نام و نام خانوادگی')),
                ('mobile_phone', models.CharField(help_text='ضروری', max_length=11, verbose_name='شماره تلفن همراه')),
                ('email', models.EmailField(help_text='ضروری', max_length=255, verbose_name='آدرس ایمیل')),
                ('body', models.TextField(help_text='ضروری', max_length=1000, verbose_name='بدنه')),
            ],
            options={
                'verbose_name': 'پیام',
                'verbose_name_plural': 'پیام ها',
            },
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(help_text='ضروری', max_length=500, verbose_name='بدنه')),
                ('user', models.ForeignKey(help_text='ضروری', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'شکایت',
                'verbose_name_plural': 'شکایات',
            },
        ),
    ]
