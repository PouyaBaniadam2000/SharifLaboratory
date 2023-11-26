# Generated by Django 4.2.6 on 2023-11-26 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='ضروری', max_length=50, verbose_name='گواهینامه')),
                ('image', models.ImageField(help_text='ضروری', upload_to='home/Certificate/images', verbose_name='تصویر')),
                ('is_allowed', models.BooleanField(default=True, verbose_name='مجوز نشان داده شدن دارد؟')),
            ],
            options={
                'verbose_name': 'گواهینامه',
                'verbose_name_plural': 'گواهینامه ها',
            },
        ),
        migrations.CreateModel(
            name='GeneralWebsiteIdea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='ضروری', max_length=50, verbose_name='تیتر')),
                ('body', models.TextField(help_text='ضروری', max_length=500, verbose_name='بدنه')),
            ],
            options={
                'verbose_name': 'ایده کلی',
                'verbose_name_plural': 'ایده های کلی',
            },
        ),
        migrations.CreateModel(
            name='GeneralWebsiteIdeaImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='ضروری', max_length=100, verbose_name='تیتر (نمایش داده نمی شود.)')),
                ('image', models.ImageField(help_text='ضروری', upload_to='home/general website idea image/images', verbose_name='تصویر')),
            ],
            options={
                'verbose_name': 'تصویر ایده کلی سایت',
                'verbose_name_plural': 'تصاویر ایده کلی سایت',
            },
        ),
        migrations.CreateModel(
            name='SharifLabServicePreview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(help_text='ضروری', upload_to='home/sharif lab service preview/images', verbose_name='آیکون')),
                ('title', models.CharField(help_text='ضروری', max_length=50, verbose_name='تیتر')),
                ('body', models.TextField(help_text='ضروری', max_length=500, verbose_name='بدنه')),
            ],
            options={
                'verbose_name': 'پری ویو خدمت آزمایشگاه شریف',
                'verbose_name_plural': 'پری ویو های خدمات آزمایشگاه شریف',
            },
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='ضروری', max_length=100, verbose_name='نام و نام خانوادگی')),
                ('role', models.CharField(help_text='ضروری', max_length=100, verbose_name='نقش')),
                ('about', models.TextField(help_text='ضروری', max_length=1000, verbose_name='درباره')),
                ('image', models.ImageField(help_text='ضروری', upload_to='home/team member/images', verbose_name='تصویر')),
            ],
            options={
                'verbose_name': 'عضو تیم',
                'verbose_name_plural': 'اعضای تیم',
            },
        ),
    ]
