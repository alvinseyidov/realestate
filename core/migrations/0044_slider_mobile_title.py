# Generated by Django 4.2.6 on 2024-01-26 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0043_slider_black_layer_css_mobile_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='mobile_title',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
