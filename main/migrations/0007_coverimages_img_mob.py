# Generated by Django 5.1.3 on 2024-12-14 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_coverimages_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='coverimages',
            name='img_mob',
            field=models.URLField(default='', verbose_name='Mobil versiya üçün şəkil'),
        ),
    ]
