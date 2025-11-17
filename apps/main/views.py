from django.shortcuts import render
from django.views.generic import TemplateView


class Home(TemplateView):
    # return render(request, 'main/home.html')
    template_name = 'main/home.html'
