# Generated by Django 4.2.6 on 2023-10-29 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statik', '0008_processessection_process1_icon_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainsection',
            name='number1',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='mainsection',
            name='number1_text',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='mainsection',
            name='number2',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='mainsection',
            name='number2_text',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
