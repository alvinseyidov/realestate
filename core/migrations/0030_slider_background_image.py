# Generated by Django 4.2.6 on 2024-01-08 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_slider'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='background_image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
