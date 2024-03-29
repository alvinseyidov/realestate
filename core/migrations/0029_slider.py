# Generated by Django 4.2.6 on 2024-01-08 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_general_logo_white'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('text', models.TextField()),
                ('button_text', models.CharField(max_length=256)),
                ('button_url', models.CharField(max_length=256)),
            ],
        ),
    ]
