# Generated by Django 4.2.6 on 2024-01-11 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_parametr_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='general',
            name='favicon',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
