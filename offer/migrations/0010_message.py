# Generated by Django 4.2.6 on 2023-12-26 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0009_alter_offer_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('phone', models.CharField(max_length=256)),
                ('email', models.CharField(max_length=256)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name': 'Ev, Villa Müraciət Edən',
                'verbose_name_plural': 'Evlər, Villalar  Müraciət Edənlər',
            },
        ),
    ]
