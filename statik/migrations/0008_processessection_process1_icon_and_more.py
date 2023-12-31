# Generated by Django 4.2.6 on 2023-10-29 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statik', '0007_sortingsections'),
    ]

    operations = [
        migrations.AddField(
            model_name='processessection',
            name='process1_icon',
            field=models.FileField(default='1', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='processessection',
            name='process2_icon',
            field=models.FileField(default='1', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='processessection',
            name='process3_icon',
            field=models.FileField(default='1', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='processessection',
            name='process4',
            field=models.CharField(default='1', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='processessection',
            name='process4_icon',
            field=models.FileField(default='1', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='processessection',
            name='process5',
            field=models.CharField(default='1', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='processessection',
            name='process5_icon',
            field=models.FileField(default='1', upload_to=''),
            preserve_default=False,
        ),
    ]
