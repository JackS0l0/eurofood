from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
class About(models.Model):
    txt=RichTextField('Haqqımızda məlumat')
    def __str__(self):
        return self.txt
    class Meta:
        verbose_name = 'Haqqımızda'
        verbose_name_plural = 'Haqqımızda'
class Contact(models.Model):
    txt=RichTextField('Əlaqə məlumatları')
    def __str__(self):
        return self.txt
    class Meta:
        verbose_name = 'Əlaqə məlumatları'
        verbose_name_plural = 'Əlaqə məlumatları'
class CoverImages(models.Model):
    name=models.CharField('Ad',max_length=200)
    img=models.URLField('Şəkil',default='')
    img_mob=models.URLField('Mobil versiya üçün şəkil',default='')
    date=models.DateTimeField('Tarix',default=timezone.now)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Kover şəkil'
        verbose_name_plural = 'Kover şəkillər'