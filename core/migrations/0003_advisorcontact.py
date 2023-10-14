# Generated by Django 4.2.6 on 2023-10-13 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_social'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvisorContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('surname', models.CharField(max_length=256)),
                ('phone', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Advisora müraicət',
                'verbose_name_plural': 'Advisora müraicətlər',
            },
        ),
    ]
