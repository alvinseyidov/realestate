# Generated by Django 4.2.6 on 2024-02-15 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('statik', '0033_remove_coffeesection_datetime'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvantageSectionRU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CoffeeSectionRU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('button_text', models.CharField(max_length=256)),
                ('user1_image', models.ImageField(upload_to='')),
                ('user1_name', models.CharField(max_length=256)),
                ('user1_profession', models.CharField(max_length=256)),
                ('user2_image', models.ImageField(upload_to='')),
                ('user2_name', models.CharField(max_length=256)),
                ('user2_profession', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Coffee Section',
                'verbose_name_plural': 'Ru Coffee Section',
            },
        ),
        migrations.CreateModel(
            name='FeedbackSectionRU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Müştəri Geribildirim Bölməsi',
                'verbose_name_plural': 'Ru    Müştəri Geribildirim Bölməsi',
            },
        ),
        migrations.CreateModel(
            name='Form1RU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('sub_title', models.CharField(max_length=256)),
                ('success_text', models.CharField(max_length=256)),
                ('button_text', models.CharField(max_length=256)),
                ('text1', models.CharField(max_length=256)),
                ('text2', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Form Vebinara Yazıl',
                'verbose_name_plural': 'Ru Form - Vebinara Yazıl',
            },
        ),
        migrations.CreateModel(
            name='Form2RU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('success_text', models.CharField(max_length=256)),
                ('button_text', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Form Listing',
                'verbose_name_plural': 'Ru Form - Listing',
            },
        ),
        migrations.CreateModel(
            name='Form3RU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('success_text', models.CharField(max_length=256)),
                ('button_text', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Form Özün tapmısan',
                'verbose_name_plural': 'Ru Form - Özün tapmısan',
            },
        ),
        migrations.CreateModel(
            name='Form4RU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('sub_title', models.CharField(max_length=256)),
                ('success_text', models.CharField(max_length=256)),
                ('button_text', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Form Property Viewing',
                'verbose_name_plural': 'Ru Form - Property Viewing',
            },
        ),
        migrations.CreateModel(
            name='FormSectionRU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('sub_title', models.CharField(max_length=256)),
                ('text', models.TextField()),
                ('form_button_text', models.CharField(max_length=256)),
                ('form_button_link', models.CharField(max_length=256)),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'Form Bölməsi',
                'verbose_name_plural': 'Ru     Form Bölməsi',
            },
        ),
        migrations.CreateModel(
            name='GeliriHesablaBannerRU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=256)),
                ('background_image', models.ImageField(upload_to='')),
                ('button_text', models.CharField(max_length=256)),
                ('button_link', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Gəliri Hesablə Banneri',
                'verbose_name_plural': 'Ru           Gəliri Hesablə Banneri',
            },
        ),
        migrations.CreateModel(
            name='GetConsultationSectionRU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('text', models.TextField()),
                ('button_text', models.CharField(max_length=256)),
                ('button_link', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='MainSectionRU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('text', models.TextField()),
                ('text2', models.TextField()),
                ('text3', models.TextField()),
                ('button_text', models.CharField(max_length=256)),
                ('button_link', models.CharField(max_length=256)),
                ('background_image', models.FileField(upload_to='')),
            ],
            options={
                'verbose_name': 'Əsas Bölmə (1-ci bölmə)',
                'verbose_name_plural': 'Ru              Əsas Bölmə (1-ci bölmə)',
            },
        ),
        migrations.CreateModel(
            name='MuzakireEdekRU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('text', models.TextField()),
                ('button_text', models.CharField(max_length=256)),
                ('button_link', models.CharField(max_length=256)),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'Calendly Bölməsi',
                'verbose_name_plural': 'Ru   Calendly Bölməsi',
            },
        ),
        migrations.CreateModel(
            name='NiyeSecirlerRU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('title1', models.CharField(max_length=256)),
                ('text1', models.TextField()),
                ('title2', models.CharField(max_length=256)),
                ('text2', models.TextField()),
                ('title3', models.CharField(max_length=256)),
                ('text3', models.TextField()),
                ('title4', models.CharField(max_length=256)),
                ('text4', models.TextField()),
            ],
            options={
                'verbose_name': 'Niyə Bizi Seçirlər Punkt',
                'verbose_name_plural': 'Ru       Niyə Bizi Seçirlər Punktlar',
            },
        ),
        migrations.CreateModel(
            name='OffersSectionRU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('text', models.TextField()),
                ('form_text', models.CharField(max_length=256)),
                ('form_button_text', models.CharField(max_length=256)),
                ('form_button_url', models.CharField(max_length=256)),
                ('title2', models.CharField(max_length=256, verbose_name='Offer səhifəsində başlıq')),
                ('title3', models.CharField(max_length=256, verbose_name='Offer səhifəsində alt başlıq')),
            ],
            options={
                'verbose_name': 'Evlər, Villalar Bölməsi',
                'verbose_name_plural': 'Ru      Evlər, Villalar Bölməsi',
            },
        ),
        migrations.CreateModel(
            name='PagesRU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('link', models.CharField(max_length=256)),
                ('body', models.TextField()),
            ],
            options={
                'verbose_name': ' Statik səhifələr',
                'verbose_name_plural': 'Ru  Statik səhifələr',
            },
        ),
        migrations.CreateModel(
            name='ProcessesSectionRU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('process1_title', models.CharField(max_length=256)),
                ('process1_text', models.CharField(max_length=256)),
                ('process1_icon', models.FileField(upload_to='')),
                ('process2_title', models.CharField(max_length=256)),
                ('process2_text', models.CharField(max_length=256)),
                ('process2_icon', models.FileField(upload_to='')),
                ('process3_title', models.CharField(max_length=256)),
                ('process3_text', models.CharField(max_length=256)),
                ('process3_icon', models.FileField(upload_to='')),
                ('process4_title', models.CharField(max_length=256)),
                ('process4_text', models.CharField(max_length=256)),
                ('process4_icon', models.FileField(upload_to='')),
            ],
            options={
                'verbose_name': 'Proseslər Bölməsi',
                'verbose_name_plural': 'Ru            Proseslər Bölməsi',
            },
        ),
        migrations.CreateModel(
            name='SliderSectionRU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name': 'Slider Bölmə',
                'verbose_name_plural': 'Ru             Slider Bölmə',
            },
        ),
        migrations.CreateModel(
            name='SmartInvestRU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('text', models.CharField(max_length=256)),
                ('button_text', models.CharField(max_length=256)),
                ('button_link', models.CharField(max_length=256)),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'Niyə Smart İnvest Bölməsi',
                'verbose_name_plural': 'Ru         Niyə Smart İnvest Bölməsi',
            },
        ),
        migrations.CreateModel(
            name='SortingSectionsRU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_section_active', models.BooleanField(default=True)),
                ('main_section_sort', models.IntegerField()),
                ('youtube_video_active', models.BooleanField(default=True)),
                ('youtube_video_sort', models.IntegerField()),
                ('why_active', models.BooleanField(default=True)),
                ('why_sort', models.IntegerField()),
                ('advantages_active', models.BooleanField(default=True)),
                ('advantages_sort', models.IntegerField()),
                ('processes_active', models.BooleanField(default=True)),
                ('processes_sort', models.IntegerField()),
                ('get_consultation_active', models.BooleanField(default=True)),
                ('get_consultation_sort', models.IntegerField()),
                ('faq_active', models.BooleanField(default=True)),
                ('faq_sort', models.IntegerField()),
                ('offers_active', models.BooleanField(default=True)),
                ('offers_sort', models.IntegerField()),
                ('feedbacks_active', models.BooleanField(default=True)),
                ('feedbacks_sort', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SuallarRU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=256)),
                ('link', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Banner üzərindəki sual',
                'verbose_name_plural': 'Ru          Banner üzərindəki suallar',
            },
        ),
        migrations.CreateModel(
            name='WhySectionRU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name': 'Komanda Bölməsi',
                'verbose_name_plural': 'Ru  Komanda Bölməsi',
            },
        ),
        migrations.CreateModel(
            name='PunktlarRU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('m', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='punktlar', to='statik.muzakireedekru')),
            ],
        ),
    ]