# Generated by Django 4.2.6 on 2024-02-07 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('statik', '0032_rename_dateime_coffeesection_datetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coffeesection',
            name='datetime',
        ),
    ]
