# Generated by Django 4.2.6 on 2023-11-06 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratory', '0007_remove_laboratory_parent_laboratory_has_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(help_text='ضروری', max_length=100, verbose_name='کتگوری')),
                ('is_allowed', models.BooleanField(default=True, verbose_name='مجوز نشان داده شدن دارد؟')),
            ],
            options={
                'verbose_name': 'کتگوری',
                'verbose_name_plural': 'کتگوری ها',
            },
        ),
        migrations.RemoveField(
            model_name='laboratory',
            name='date',
        ),
        migrations.RemoveField(
            model_name='laboratory',
            name='financial_value',
        ),
        migrations.RemoveField(
            model_name='laboratory',
            name='location',
        ),
        migrations.AddField(
            model_name='laboratory',
            name='categories',
            field=models.ManyToManyField(help_text='ضروری', related_name='weblogs', to='laboratory.category', verbose_name='کتگوری ها'),
        ),
    ]