# Generated by Django 4.2.6 on 2024-02-05 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('statik', '0031_coffeesection'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coffeesection',
            old_name='dateime',
            new_name='datetime',
        ),
    ]
