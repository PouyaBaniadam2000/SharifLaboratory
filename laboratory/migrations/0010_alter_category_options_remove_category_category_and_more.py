# Generated by Django 4.2.6 on 2023-11-09 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laboratory', '0009_remove_laboratory_has_child_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'دسته بندی', 'verbose_name_plural': 'دسته بندی ها'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='category',
        ),
        migrations.RemoveField(
            model_name='category',
            name='is_allowed',
        ),
        migrations.RemoveField(
            model_name='laboratory',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='laboratory',
            name='record_preview',
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=1, help_text='ضروری', max_length=150, verbose_name='اسلاگ (متن داخل URL)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='title',
            field=models.CharField(default=1, help_text='ضروری', max_length=100, verbose_name='تیتر'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='laboratory',
            name='category',
            field=models.ForeignKey(default=1, help_text='ضروری', on_delete=django.db.models.deletion.CASCADE, to='laboratory.category', verbose_name='دسته بندی'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='laboratory',
            name='laboratory_preview',
            field=models.CharField(default=1, help_text='ضروری', max_length=200, verbose_name='درباره آزمایشگاه'),
            preserve_default=False,
        ),
    ]