# Generated by Django 4.2.6 on 2024-01-10 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_alter_slider_options_slider_sorting'),
    ]

    operations = [
        migrations.AddField(
            model_name='parametr',
            name='title',
            field=models.CharField(default=1, max_length=256, verbose_name='Bölmənin başlığı'),
            preserve_default=False,
        ),
    ]