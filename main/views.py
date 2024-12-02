from django.shortcuts import render
from products.models import Products,Brands,Categories
from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.views.generic import ListView
from django.utils import translation
from django.db.models import Q
def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response
def index(request):
    data={
        'title': 'EuroFood',
        'products':Products.objects.all().order_by('-date'),
        'brands':Brands.objects.all(),
        'categories':Categories.objects.all(),
    }
    return render(request, 'index.html',data)
class SearchForm(ListView):
    model = Products
    context_object_name = 'products'
    template_name = 'search.html'
    def get_context_data(self, **kwargs):
        context=super(SearchForm, self).get_context_data(**kwargs)
        query = self.request.GET.get('q')
        if query:
            context['title'] = 'Axtarış nəticəsi'
            context['products'] = Products.objects.filter(Q(name__icontains=query)).order_by('-date')[0:8]
            context['categories'] = Categories.objects.all().order_by('name')
            context['brands'] = Brands.objects.all().order_by('name')
            return context