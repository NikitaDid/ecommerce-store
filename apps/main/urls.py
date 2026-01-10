from django.urls import path
from apps.catalog import views as catalog_views
from apps.main.views import PageView, index

urlpatterns = [
    path('', index, name='home'),
    path('<str:slug>/', PageView.as_view(), name='page'),
    path('catalog/', catalog_views.CategoryIndexView.as_view(), name='catalog:index'),
    path('catalog/<slug:slug>/', catalog_views.ProductDetailView.as_view(), name='catalog:product'),

]
