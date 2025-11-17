from xml.etree.ElementInclude import include

from django.urls import path
from django.urls import path
from apps.main import views as main_views
from apps.catalog import views as catalog_views

urlpatterns = [
    path('', main_views.Home.as_view(), name='home'),
    path('catalog/', catalog_views.CategoryIndexView.as_view(), name='catalog:index'),
    path('catalog/<slug:slug>/', catalog_views.ProductDetailView.as_view(), name='catalog:product'),

]