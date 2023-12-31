# Generated by Django 4.2.6 on 2023-10-14 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0004_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='distance_to_airport',
            field=models.CharField(default='1', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offer',
            name='distance_to_beach',
            field=models.CharField(default='1', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offer',
            name='distance_to_center',
            field=models.CharField(default='1', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offer',
            name='installment',
            field=models.CharField(default='1', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offer',
            name='project_status',
            field=models.CharField(default='1', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offer',
            name='sea_view',
            field=models.CharField(default='1', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offer',
            name='state_guaranteed',
            field=models.CharField(default='1', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offer',
            name='suitable_for_citizenship',
            field=models.CharField(default='1', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offer',
            name='year_built',
            field=models.CharField(default='1', max_length=256),
            preserve_default=False,
        ),
    ]
