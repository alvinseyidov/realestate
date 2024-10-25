# Generated by Django 5.1 on 2024-10-25 17:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0023_offer_mertebe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='offer',
            name='elave_sahe',
            field=models.CharField(choices=[('H', 'Həyət'), ('T', 'Terras'), ('B', 'Balkon')], default='H', max_length=2),
        ),
        migrations.AlterField(
            model_name='offer',
            name='bed',
            field=models.CharField(max_length=256, verbose_name='Otaq sayı'),
        ),
        migrations.AddField(
            model_name='offer',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='offer.location'),
        ),
    ]
