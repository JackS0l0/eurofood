from .models import About,Contact
from modeltranslation.translator import TranslationOptions,register
@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ['txt']
@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = ['txt']