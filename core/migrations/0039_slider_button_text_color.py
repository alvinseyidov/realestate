# Generated by Django 4.2.6 on 2024-01-17 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_slider_black_layer_slider_button_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='button_text_color',
            field=models.CharField(choices=[('B', 'Black'), ('W', 'White')], default='B', max_length=1),
        ),
    ]