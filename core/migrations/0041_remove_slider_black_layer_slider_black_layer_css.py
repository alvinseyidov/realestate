# Generated by Django 4.2.6 on 2024-01-17 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_alter_slider_button_color_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slider',
            name='black_layer',
        ),
        migrations.AddField(
            model_name='slider',
            name='black_layer_css',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
