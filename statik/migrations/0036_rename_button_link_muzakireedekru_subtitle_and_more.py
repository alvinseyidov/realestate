# Generated by Django 4.2.6 on 2024-03-07 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('statik', '0035_advantagesectiontr_coffeesectiontr_feedbacksectiontr_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='muzakireedekru',
            old_name='button_link',
            new_name='subtitle',
        ),
        migrations.RenameField(
            model_name='muzakireedektr',
            old_name='button_link',
            new_name='subtitle',
        ),
        migrations.RemoveField(
            model_name='muzakireedekru',
            name='button_text',
        ),
        migrations.RemoveField(
            model_name='muzakireedekru',
            name='image',
        ),
        migrations.RemoveField(
            model_name='muzakireedekru',
            name='text',
        ),
        migrations.RemoveField(
            model_name='muzakireedektr',
            name='button_text',
        ),
        migrations.RemoveField(
            model_name='muzakireedektr',
            name='image',
        ),
        migrations.RemoveField(
            model_name='muzakireedektr',
            name='text',
        ),
    ]
