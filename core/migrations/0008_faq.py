# Generated by Django 4.2.6 on 2023-10-14 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_general_telegram_link_general_whatsapp_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=256)),
                ('answer', models.CharField(max_length=256)),
                ('sort', models.IntegerField()),
            ],
            options={
                'ordering': ('sort',),
            },
        ),
    ]