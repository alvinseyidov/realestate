# Generated by Django 4.2.6 on 2024-02-15 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0045_feedbacktr_slidertr'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQRU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=256)),
                ('answer', models.CharField(max_length=256)),
                ('sort', models.IntegerField()),
            ],
            options={
                'verbose_name': 'FAQ Sual',
                'verbose_name_plural': 'RU FAQ Suallar',
                'ordering': ('sort',),
            },
        ),
        migrations.CreateModel(
            name='FeatureRU',
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
                'verbose_name_plural': 'RU Niyə? Səbəblər',
            },
        ),
        migrations.CreateModel(
            name='FeedbackRU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_image', models.ImageField(upload_to='')),
                ('full_name', models.CharField(max_length=256)),
                ('position', models.CharField(max_length=256)),
                ('text', models.TextField()),
                ('background_image', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'Ru Müştəri Geri Bildirim',
                'verbose_name_plural': 'Ru Müştəri Geri Bildirimləri',
            },
        ),
        migrations.CreateModel(
            name='GeneralRU',
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
                'verbose_name_plural': 'Ru Ümumi Sayt Məlumatlar',
            },
        ),
        migrations.CreateModel(
            name='SliderRU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background_image', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=256)),
                ('mobile_title', models.CharField(blank=True, max_length=256, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('button_text', models.CharField(blank=True, max_length=256, null=True)),
                ('button_url', models.CharField(blank=True, max_length=256, null=True)),
                ('button_color', models.CharField(choices=[('B', 'black'), ('W', 'white')], default='W', max_length=1)),
                ('button_text_color', models.CharField(choices=[('B', 'black'), ('W', 'white')], default='B', max_length=1)),
                ('image_link', models.CharField(blank=True, max_length=256, null=True)),
                ('sorting', models.IntegerField(default=1)),
                ('black_layer_css', models.CharField(blank=True, default='background: linear-gradient(90deg, #000 33.33%, rgba(0, 0, 0, 0.00) 99.89%)', max_length=256, null=True)),
                ('black_layer_css_mobile', models.CharField(blank=True, default='background: linear-gradient(180deg, #000 33.33%, rgba(0, 0, 0, 0.00) 99.89%)', max_length=256, null=True)),
            ],
            options={
                'verbose_name': 'Ru Slider',
                'verbose_name_plural': 'Ru Slider',
                'ordering': ('sorting',),
            },
        ),
        migrations.CreateModel(
            name='WhyRU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.FileField(upload_to='')),
                ('title', models.CharField(max_length=256)),
                ('text', models.CharField(max_length=256)),
                ('position', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Komanda üzvü',
                'verbose_name_plural': 'Ru Komanda',
            },
        ),
        migrations.AlterModelOptions(
            name='feedbacktr',
            options={'verbose_name': 'Türkçə Müştəri Geri Bildirim', 'verbose_name_plural': 'Türkçə Müştəri Geri Bildirimləri'},
        ),
        migrations.AlterModelOptions(
            name='slidertr',
            options={'ordering': ('sorting',), 'verbose_name': 'Türkçə Slider', 'verbose_name_plural': 'Türkçə Slider'},
        ),
    ]
