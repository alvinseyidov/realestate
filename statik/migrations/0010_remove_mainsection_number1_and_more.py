# Generated by Django 4.2.6 on 2023-12-02 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statik', '0009_alter_mainsection_number1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainsection',
            name='number1',
        ),
        migrations.RemoveField(
            model_name='mainsection',
            name='number1_text',
        ),
        migrations.RemoveField(
            model_name='mainsection',
            name='number2',
        ),
        migrations.RemoveField(
            model_name='mainsection',
            name='number2_text',
        ),
        migrations.AddField(
            model_name='mainsection',
            name='text2',
            field=models.TextField(default='1'),
            preserve_default=False,
        ),
    ]
