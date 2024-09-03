# Generated by Django 4.2.6 on 2024-03-14 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statik', '0036_rename_button_link_muzakireedekru_subtitle_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='muzakireedek',
            name='button_link',
        ),
        migrations.RemoveField(
            model_name='muzakireedek',
            name='button_text',
        ),
        migrations.RemoveField(
            model_name='muzakireedek',
            name='image',
        ),
        migrations.RemoveField(
            model_name='muzakireedek',
            name='text',
        ),
        migrations.AddField(
            model_name='muzakireedek',
            name='subtitle',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
    ]