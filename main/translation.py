from products.models import Products,Categories,Brands
from modeltranslation.translator import TranslationOptions,register
@register(Products)
class ProductsTranslationOptions(TranslationOptions):
    fields = ['name', 'desc']
@register(Categories)
class CategoriesTranslationOptions(TranslationOptions):
    fields = ['name']
@register(Brands)
class BrandsTranslationOptions(TranslationOptions):
    fields = ['name']