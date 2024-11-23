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
# class CategoriesList(ListView):
#     model = Products
#     template_name = 'categories.html'
#     context_object_name = 'products'
#     def get_queryset(self):
#         queryset = super(CategoriesList, self).get_queryset()
#         category_id = self.kwargs.get('category_id')
#         return queryset.filter(category_id=category_id) if category_id else queryset
#     def get_context_data(self, **kwargs):
#         data=super(CategoriesList,self).get_context_data(**kwargs)
#         data['title']='Categories'
#         data['categories']=Categories.objects.all().order_by('name')
#         data['brands']=Brands.objects.all().order_by('name')
#         data['products']=Products.objects.all().order_by('-date')
#         return data
# class BrandsList(ListView):
#     model = Products
#     template_name = 'brands.html'
#     context_object_name = 'products'
#     def get_queryset(self):
#         queryset = super(BrandsList, self).get_queryset()
#         brand_id = self.kwargs.get('brand_id')
#         return queryset.filter(brand_id=brand_id) if brand_id else queryset
#     def get_context_data(self, **kwargs):
#         data=super(BrandsList,self).get_context_data(**kwargs)
#         data['title']='Brands'
#         data['categories']=Categories.objects.all().order_by('name')
#         data['brands']=Brands.objects.all().order_by('name')
#         data['products']=Products.objects.all().order_by('-date')
#         return data