from django.contrib import admin
from django import forms
from .models import Brand, Model, Product, ProductModel


class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(Brand, BrandAdmin)


class ModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(Model, ModelAdmin)


class ProductAdmin(admin.ModelAdmin):
    fields = ['brand', 'name', 'slug', 'created_at', 'updated_at']
    list_display = ['name', 'brand', 'slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(Product, ProductAdmin)


class ProductModelAdmin(admin.ModelAdmin):
    fields = ['product', 'model', 'slug', 'created_at', 'updated_at']
    list_display = ['slug', 'product', 'model', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(ProductModel, ProductModelAdmin)
