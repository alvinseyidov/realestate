# Generated by Django 4.2.6 on 2023-10-29 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('statik', '0004_alter_mainsection_title1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mainsection',
            old_name='title1',
            new_name='title',
        ),
    ]