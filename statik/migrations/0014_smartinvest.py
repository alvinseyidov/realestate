# Generated by Django 4.2.6 on 2023-12-02 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statik', '0013_suallar'),
    ]

    operations = [
        migrations.CreateModel(
            name='SmartInvest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('text', models.CharField(max_length=256)),
                ('button_text', models.CharField(max_length=256)),
                ('button_link', models.CharField(max_length=256)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
