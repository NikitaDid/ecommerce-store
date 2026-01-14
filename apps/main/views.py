from django.shortcuts import render
from django.template.context_processors import request
from django.views import generic
from apps.main.models import Page, ProductSet


def index(request):
    page = Page.objects.get(slug='home')
    products_sets = ProductSet.objects.filter(is_active=True)
    return render(request, "main/home.html", {'page': page, 'products_sets': products_sets})


class PageView(generic.DetailView):
    model = Page
    template_name = 'main/page.html'
    queryset = Page.objects.all()


