from django.contrib import admin
from django.urls import path,re_path
from main import views as mainviews
from products import views as productsviews
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('product/<slug:slug>/<int:pk>/',productsviews.ProductDetailViews.as_view(),name='postdetail'),
    path('category/<int:category_id>/',productsviews.CategoriesList, name='categoriesdetail'),
    path('brands/<int:brand_id>/',productsviews.BrandsList,name='brandsdetail'),
    path('search_res/', mainviews.SearchForm.as_view(), name='searchpage'),
    path('admin/', admin.site.urls),
    path('',mainviews.index,name='homepage'),
]
urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language=False),
    path("set_language/<str:language>", mainviews.set_language, name="set-language"),
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)