from django.contrib import admin
from django import forms
from .models import Brand, Model, Product, ProductModel


class BrandAdminForm(forms.ModelForm):

    class Meta:
        model = Brand
        fields = '__all__'


class BrandAdmin(admin.ModelAdmin):
    form = BrandAdminForm
    list_display = ['name', 'slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(Brand, BrandAdmin)


class ModelAdminForm(forms.ModelForm):

    class Meta:
        model = Model
        fields = '__all__'


class ModelAdmin(admin.ModelAdmin):
    form = ModelAdminForm
    list_display = ['name', 'slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(Model, ModelAdmin)


class ProductAdminForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    fields = ['brand', 'name', 'slug', 'created_at', 'updated_at']
    list_display = ['brand', 'name', 'slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(Product, ProductAdmin)


class ProductModelAdminForm(forms.ModelForm):

    class Meta:
        model = ProductModel
        fields = '__all__'


class ProductModelAdmin(admin.ModelAdmin):
    form = ProductModelAdminForm
    fields = ['product', 'model', 'slug', 'created_at', 'updated_at']
    list_display = ['slug', 'product', 'model', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(ProductModel, ProductModelAdmin)
