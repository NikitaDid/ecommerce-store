from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from apps.catalog.models import Product
from apps.user.models import User


class Cart(models.Model):
    product = models.ForeignKey(Product, verbose_name="Product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Quantity')
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'


class Order(models.Model):
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    total = models.DecimalField(verbose_name='Total', max_digits=12, decimal_places=2)
    first_name = models.CharField(verbose_name='Name', max_length=255)
    last_name = models.CharField(verbose_name='Last name', max_length=255)
    email = models.EmailField(verbose_name='E-mail')
    phone = PhoneNumberField(verbose_name='Phone')
    address = models.TextField(verbose_name='Address')
    comments = models.TextField(verbose_name='Comment', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='Creation data', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Update data', auto_now=True)


    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, verbose_name='Order', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='product', null=True, on_delete=models.SET_NULL)
    price = models.DecimalField(verbose_name='Price', max_digits=12, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name='Quantity')


    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
