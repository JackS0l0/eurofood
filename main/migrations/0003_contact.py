# Generated by Django 5.1.3 on 2024-12-11 02:09

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_about_txt_az_about_txt_en_about_txt_ru'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txt', ckeditor.fields.RichTextField(verbose_name='Əlaqə məlumatları')),
            ],
            options={
                'verbose_name': 'Əlaqə məlumatları',
                'verbose_name_plural': 'Əlaqə məlumatları',
            },
        ),
    ]
