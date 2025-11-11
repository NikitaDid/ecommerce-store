from django.shortcuts import render

from apps.catalog.models import Category, Product
from django.views import generic


class CategoryIndexView(generic.ListView):
    model = Category
    template_name = 'catalog/index.html'  #Check if changes needed
    queryset = Category.objects.filter(parent=None)  # only want top-level categories


class ProductsByCategoryView(generic.ListView):
    template_name = 'catalog/category.html'
    category = None
    categories = Category.objects.all()


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'catalog/product.html'
