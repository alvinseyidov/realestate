# Generated by Django 4.2.6 on 2023-12-15 20:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_waitlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='general',
            name='countdown_enddate',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
