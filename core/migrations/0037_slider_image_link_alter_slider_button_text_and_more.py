# Generated by Django 4.2.6 on 2024-01-15 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_calendlyscript'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='image_link',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='slider',
            name='button_text',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='slider',
            name='button_url',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
