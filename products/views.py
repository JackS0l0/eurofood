from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView,ListView
from .models import Categories,Brands,Products
from django.core.paginator import Paginator
class ProductDetailViews(DetailView):
    model = Products
    template_name = 'post.html'
    context_object_name = 'products'
    def get_context_data(self, **kwargs):
        data=super(ProductDetailViews, self).get_context_data(**kwargs)
        data['title']=self.object.name
        data['categories']=Categories.objects.all().order_by('name')
        data['brands']=Brands.objects.all().order_by('name')
        data['products']=Products.objects.all().order_by('-date')
        return data
def CategoriesList(request, category_id, page_number=1):
    if category_id:
        category = Categories.objects.get(id=category_id)
        products = Products.objects.filter(category=category).order_by('-date')
    else:
        products = Products.objects.all().order_by('-date')
    pagi = Paginator(products, 15)
    page_number = request.GET.get('page')
    page_pagi = pagi.get_page(page_number)
    data = {
        'title': 'Categories',
        'categories': Categories.objects.all().order_by('name'),
        'brands': Brands.objects.all().order_by('name'),
        'products': page_pagi,
    }
    return render(request, 'categories.html', data)
def BrandsList(request, brand_id, page_number=1):
    if brand_id:
        brand = Brands.objects.get(id=brand_id)
        products = Products.objects.filter(brand=brand).order_by('-date')
    else:
        products = Products.objects.all().order_by('-date')
    pagi = Paginator(products, 15)
    page_number = request.GET.get('page')
    page_pagi = pagi.get_page(page_number)
    data = {
        'title': 'Brands',
        'categories': Categories.objects.all().order_by('name'),
        'brands': Brands.objects.all().order_by('name'),
        'products': page_pagi,
    }
    return render(request, 'brands.html', data)
def products(request, category_id=None, page_number=1):
    products=Products.objects.filter(article_category_id=category_id).order_by('-date') if category_id else Products.objects.all().order_by('-date')
    pagi = Paginator(products, 15)
    page_number = request.GET.get('page')
    page_pagi = pagi.get_page(page_number)
    data={
        'title': 'All Products',
        'categories': Categories.objects.all().order_by('name'),
        'brands': Brands.objects.all().order_by('name'),
        'products': page_pagi
    }
    return render(request, 'allproducts.html',data)