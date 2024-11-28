from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView,ListView
from .models import Categories,Brands,Products
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
def CategoriesList(request, category_id):
    if category_id:
        category = Categories.objects.get(id=category_id)
        products = Products.objects.filter(category=category)
    else:
        products = Products.objects.all().order_by('-date')
    data={
        'title': 'Categories',
        'categories': Categories.objects.all().order_by('name'),
        'brands': Brands.objects.all().order_by('name'),
        'products': products,
    }
    return render(request, 'categories.html',data)
def BrandsList(request, brand_id):
    if brand_id:
        brand = Brands.objects.get(id=brand_id)
        products = Products.objects.filter(brand=brand)
    else:
        products = Products.objects.all().order_by('-date')
    data={
        'title': 'Categories',
        'categories': Categories.objects.all().order_by('name'),
        'brands': Brands.objects.all().order_by('name'),
        'products': products,
    }
    return render(request, 'categories.html',data)
def products(request):
    data={
        'title': 'All Products',
        'categories': Categories.objects.all().order_by('name'),
        'brands': Brands.objects.all().order_by('name'),
        'products': Products.objects.all().order_by('-date'),
    }
    return render(request, 'allproducts.html',data)