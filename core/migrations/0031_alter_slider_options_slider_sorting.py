# Generated by Django 4.2.6 on 2024-01-10 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_slider_background_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slider',
            options={'ordering': ('sorting',)},
        ),
        migrations.AddField(
            model_name='slider',
            name='sorting',
            field=models.IntegerField(default=1),
        ),
    ]