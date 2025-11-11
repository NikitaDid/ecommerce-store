from django.contrib import admin

from apps.catalog.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['name']}

#
class ProductCategoryInline(admin.TabularInline):
    model = Product.categories.through
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
    inlines = [ProductCategoryInline]
    list_display = ['id', 'name', 'quantity', 'price', 'is_checked', 'created_at']
    list_display_links = ['id', 'name']
