# Generated by Django 4.2.6 on 2024-03-08 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_vebinar_dynamic_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='dynamic_fields',
            field=models.TextField(blank=True, null=True),
        ),
    ]
