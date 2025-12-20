from django.urls import path
from apps.cart.views import add_to_cart

app_name = 'cart'

urlpatterns = [
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
]
