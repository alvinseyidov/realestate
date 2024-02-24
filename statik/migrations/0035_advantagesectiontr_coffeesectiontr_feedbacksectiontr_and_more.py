# Generated by Django 4.2.6 on 2024-02-24 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('statik', '0034_advantagesectionru_coffeesectionru_feedbacksectionru_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvantageSectionTR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CoffeeSectionTR',
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
                'verbose_name_plural': 'Tr Coffee Section',
            },
        ),
        migrations.CreateModel(
            name='FeedbackSectionTR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Müştəri Geribildirim Bölməsi',
                'verbose_name_plural': 'Tr    Müştəri Geribildirim Bölməsi',
            },
        ),
        migrations.CreateModel(
            name='Form1TR',
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
                'verbose_name_plural': 'Tr Form - Vebinara Yazıl',
            },
        ),
        migrations.CreateModel(
            name='Form2TR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('success_text', models.CharField(max_length=256)),
                ('button_text', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Form Listing',
                'verbose_name_plural': 'Tr Form - Listing',
            },
        ),
        migrations.CreateModel(
            name='Form3TR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('success_text', models.CharField(max_length=256)),
                ('button_text', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Form Özün tapmısan',
                'verbose_name_plural': 'Tr Form - Özün tapmısan',
            },
        ),
        migrations.CreateModel(
            name='Form4TR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('sub_title', models.CharField(max_length=256)),
                ('success_text', models.CharField(max_length=256)),
                ('button_text', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Form Property Viewing',
                'verbose_name_plural': 'Tr Form - Property Viewing',
            },
        ),
        migrations.CreateModel(
            name='FormSectionTR',
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
                'verbose_name_plural': 'Tr     Form Bölməsi',
            },
        ),
        migrations.CreateModel(
            name='GeliriHesablaBannerTR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=256)),
                ('background_image', models.ImageField(upload_to='')),
                ('button_text', models.CharField(max_length=256)),
                ('button_link', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Gəliri Hesablə Banneri',
                'verbose_name_plural': 'Tr           Gəliri Hesablə Banneri',
            },
        ),
        migrations.CreateModel(
            name='GetConsultationSectionTR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('text', models.TextField()),
                ('button_text', models.CharField(max_length=256)),
                ('button_link', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='MainSectionTR',
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
                'verbose_name_plural': 'Tr              Əsas Bölmə (1-ci bölmə)',
            },
        ),
        migrations.CreateModel(
            name='MuzakireEdekTR',
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
                'verbose_name_plural': 'Tr   Calendly Bölməsi',
            },
        ),
        migrations.CreateModel(
            name='NiyeSecirlerTR',
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
                'verbose_name_plural': 'Tr       Niyə Bizi Seçirlər Punktlar',
            },
        ),
        migrations.CreateModel(
            name='OffersSectionTR',
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
                'verbose_name_plural': 'Tr      Evlər, Villalar Bölməsi',
            },
        ),
        migrations.CreateModel(
            name='PagesTR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('link', models.CharField(max_length=256)),
                ('body', models.TextField()),
            ],
            options={
                'verbose_name': ' Statik səhifələr',
                'verbose_name_plural': 'Tr  Statik səhifələr',
            },
        ),
        migrations.CreateModel(
            name='ProcessesSectionTR',
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
                'verbose_name_plural': 'Tr            Proseslər Bölməsi',
            },
        ),
        migrations.CreateModel(
            name='SliderSectionTR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name': 'Slider Bölmə',
                'verbose_name_plural': 'Tr             Slider Bölmə',
            },
        ),
        migrations.CreateModel(
            name='SmartInvestTR',
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
                'verbose_name_plural': 'Tr         Niyə Smart İnvest Bölməsi',
            },
        ),
        migrations.CreateModel(
            name='SortingSectionsTR',
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
            name='SuallarTR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=256)),
                ('link', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Banner üzərindəki sual',
                'verbose_name_plural': 'Tr          Banner üzərindəki suallar',
            },
        ),
        migrations.CreateModel(
            name='WhySectionTR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name': 'Komanda Bölməsi',
                'verbose_name_plural': 'Tr  Komanda Bölməsi',
            },
        ),
        migrations.CreateModel(
            name='PunktlarTR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('m', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='punktlar', to='statik.muzakireedektr')),
            ],
        ),
    ]
