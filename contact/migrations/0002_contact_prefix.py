# Generated by Django 4.2.6 on 2024-01-15 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='prefix',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
    ]
