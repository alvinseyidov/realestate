# Generated by Django 4.2.6 on 2024-02-24 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0046_faqru_featureru_feedbackru_generalru_sliderru_whyru_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQTR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=256)),
                ('answer', models.CharField(max_length=256)),
                ('sort', models.IntegerField()),
            ],
            options={
                'verbose_name': 'FAQ Sual',
                'verbose_name_plural': 'TR FAQ Suallar',
                'ordering': ('sort',),
            },
        ),
        migrations.CreateModel(
            name='FeatureTR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=256)),
                ('icon', models.FileField(upload_to='')),
                ('description', models.TextField()),
                ('color', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Niyə? Səbəblər',
                'verbose_name_plural': 'Tr Niyə? Səbəblər',
            },
        ),
        migrations.CreateModel(
            name='GeneralTR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_title', models.CharField(max_length=256)),
                ('favicon', models.FileField(upload_to='')),
                ('meta_description', models.CharField(max_length=256)),
                ('address', models.CharField(max_length=256)),
                ('email', models.CharField(max_length=256)),
                ('phone', models.CharField(max_length=256)),
                ('whatsapp_link', models.CharField(max_length=256)),
                ('telegram_link', models.CharField(max_length=256)),
                ('copyright', models.CharField(max_length=256)),
                ('logo', models.FileField(upload_to='')),
                ('logo_white', models.FileField(blank=True, null=True, upload_to='')),
                ('home_popup_video', models.FileField(blank=True, null=True, upload_to='')),
                ('countdown_enddate', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Ümumi Sayt Məlumatlar',
                'verbose_name_plural': 'Tr Ümumi Sayt Məlumatlar',
            },
        ),
        migrations.CreateModel(
            name='WhyTR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.FileField(upload_to='')),
                ('title', models.CharField(max_length=256)),
                ('text', models.CharField(max_length=256)),
                ('position', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Komanda üzvü',
                'verbose_name_plural': 'Tr Komanda',
            },
        ),
    ]
