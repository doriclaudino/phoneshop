from django.contrib import admin
from django import forms
from .models import Brand, Model


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
