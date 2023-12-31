# Generated by Django 4.2.6 on 2023-10-14 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0003_offer_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='offer.offer')),
            ],
        ),
    ]
