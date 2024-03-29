# Generated by Django 4.2.6 on 2023-11-26 18:33

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='ضروری', max_length=100, verbose_name='تیتر')),
                ('slug', models.SlugField(allow_unicode=True, help_text='ضروری', max_length=150, verbose_name='اسلاگ (متن داخل URL)')),
                ('parent', models.ForeignKey(blank=True, help_text='ضروری', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subs', to='laboratory.category', verbose_name='والد')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='Laboratory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='ضروری', max_length=50, verbose_name='تیتر')),
                ('laboratory_preview', models.CharField(help_text='ضروری', max_length=200, verbose_name='دید کلی درباره آزمایشگاه')),
                ('image_1', models.ImageField(help_text='ضروری', upload_to='laboratory/laboratory/images', verbose_name='تصویر 1')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='laboratory/laboratory/images', verbose_name='تصویر 2')),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='laboratory/laboratory/images', verbose_name='تصویر 3')),
                ('image_4', models.ImageField(blank=True, null=True, upload_to='laboratory/laboratory/images', verbose_name='تصویر 4')),
                ('image_5', models.ImageField(blank=True, null=True, upload_to='laboratory/laboratory/images', verbose_name='تصویر 5')),
                ('image_6', models.ImageField(blank=True, null=True, upload_to='laboratory/laboratory/images', verbose_name='تصویر 6')),
                ('about_this_lab', ckeditor.fields.RichTextField(help_text='ضروری', max_length=1000, verbose_name='درباره این آزمایشگاه')),
                ('body', ckeditor.fields.RichTextField(help_text='ضروری', max_length=50000, unique=True, verbose_name='بدنه')),
                ('is_allowed', models.BooleanField(default=True, verbose_name='مجوز نشان داده شدن دارد؟')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='ایجاد شده در تاریخ')),
                ('slug', models.SlugField(allow_unicode=True, blank=True, null=True, unique=True, verbose_name='اسلاگ (متن داخل URL)')),
                ('category', models.ForeignKey(help_text='ضروری', on_delete=django.db.models.deletion.CASCADE, to='laboratory.category', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'آزمایشگاه',
                'verbose_name_plural': 'آزمایشگاه ها',
                'ordering': ('-created_at',),
            },
        ),
    ]
