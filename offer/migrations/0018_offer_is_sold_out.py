# Generated by Django 4.2.6 on 2024-02-08 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0017_alter_offer_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='is_sold_out',
            field=models.BooleanField(default=False),
        ),
    ]