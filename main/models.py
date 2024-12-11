from django.db import models
from ckeditor.fields import RichTextField
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