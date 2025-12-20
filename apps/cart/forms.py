from django import forms
from apps.cart.models import Cart


class AddToCartForm(forms.ModelForm):
     class Meta:
         model = Cart
         fields = '__all__'
