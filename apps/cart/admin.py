from django.contrib import admin

from apps.cart.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass
