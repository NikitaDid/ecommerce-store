from django.urls import path

from apps.catalog import views

urlpatterns = [
    path('<slug:slug>/', views.CategoryIndexView.as_view(), name='Catalog')
]