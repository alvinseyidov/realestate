# Generated by Django 4.2.6 on 2024-01-11 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_general_favicon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='general',
            name='countdown_enddate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='general',
            name='home_popup_video',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
