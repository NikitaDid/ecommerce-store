from django.shortcuts import render
from django.template.context_processors import request
from django.views import generic
from apps.main.models import Page


def index(request):
    return render(request, "main/home.html")


class PageView(generic.DetailView):
    model = Page
    template_name = 'main/page.html'
    queryset = Page.objects.all()
