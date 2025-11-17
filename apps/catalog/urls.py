from django.urls import path

from apps.catalog import views
from apps.catalog.views import CategoryIndexView, ProductsByCategoryView

app_name = 'catalog'

urlpatterns = [
    path('', CategoryIndexView.as_view(), name='category_list'),
    path('category/<slug:slug>/', ProductsByCategoryView.as_view(), name='category_detail')
]