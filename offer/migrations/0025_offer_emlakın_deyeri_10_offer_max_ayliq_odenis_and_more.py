# Generated by Django 5.1 on 2024-11-06 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0024_location_offer_elave_sahe_alter_offer_bed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='emlakın_deyeri_10',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='max_ayliq_odenis',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='kiraye_geliri',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
