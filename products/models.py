from django.db import models
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
class Brands(models.Model):
    name=models.CharField('Ad', max_length=200,unique=True)
    # slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL",default='brand')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Brend"
        verbose_name_plural = "Brendlər"
class Categories(models.Model):
    name=models.CharField('Ad', max_length=200,unique=True)
    icon=models.URLField('Icon', default='',null=True,blank=True)
    # slug = models.SlugField(max_length=255, unique=False, db_index=True, verbose_name="URL", default='category')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Katiqoriya"
        verbose_name_plural = "Katiqoriyalar"
class Products(models.Model):
    name=models.CharField('Məhsulun adı',max_length=200,unique=True)
    date=models.DateTimeField('Anbara daxil olma Tarixi', default=timezone.now)
    category=models.ForeignKey(to=Categories, on_delete=models.CASCADE,default='',verbose_name='Katiqoriya')
    brand=models.ForeignKey(to=Brands, on_delete=models.CASCADE,default='',verbose_name='Brend')
    img=models.URLField('Məhulun görüntüsü',default='',null=True,blank=True)
    desc=RichTextField('Məhsul haqqında',default='')
    mini_desc=RichTextField('Məzmun',default='')
    slug = models.SlugField(max_length=255, unique=False, db_index=True, verbose_name="URL",null=True,blank=True,default='products')
    def __str__(self):
        return f' {self.brand.name} {self.name}'
    class Meta:
        verbose_name = "Məhsul"
        verbose_name_plural = "Məhsullar"