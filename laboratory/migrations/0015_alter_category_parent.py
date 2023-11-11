# Generated by Django 4.2.6 on 2023-11-11 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laboratory', '0014_category_parent_alter_laboratory_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, help_text='ضروری', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subs', to='laboratory.category', verbose_name='والد'),
        ),
    ]
