from django.urls import path

from apps.catalog.views import CategoryIndexView, ProductsByCategoryView, ProductDetailView
from apps.catalog.views import create_comment

app_name = 'catalog'

urlpatterns = [
    path('', CategoryIndexView.as_view(), name='category_list'),
    path('category/<slug:slug>/', ProductsByCategoryView.as_view(), name='category_detail'),
    path('category/<slug:slug>/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('comment/<slug:slug>/<int:pk>', create_comment, name='create_comment')
]