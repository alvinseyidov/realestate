# Generated by Django 4.2.6 on 2023-12-24 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_body_head'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='body',
            options={'verbose_name': "  Body'ə əlavə olunan scriptlər", 'verbose_name_plural': "  Body'ə əlavə olunan scriptlər"},
        ),
        migrations.AlterModelOptions(
            name='head',
            options={'verbose_name': "   Head'ə əlavə olunan scriptlər", 'verbose_name_plural': "   Head'ə əlavə olunan scriptlər"},
        ),
        migrations.AddField(
            model_name='body',
            name='location',
            field=models.CharField(choices=[('T', 'After <body> tag opened'), ('B', 'Before </body> tag closed')], default='T', max_length=1),
        ),
    ]
