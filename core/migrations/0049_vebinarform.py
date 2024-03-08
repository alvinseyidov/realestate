# Generated by Django 4.2.6 on 2024-03-08 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0048_alter_faqtr_options_alter_feedbacktr_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VebinarForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=256)),
                ('placeholder', models.CharField(max_length=256)),
                ('sort', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Vebinar Dynamic Form',
                'verbose_name_plural': 'Vebinar Dynamic Form',
                'ordering': ('sort',),
            },
        ),
    ]
