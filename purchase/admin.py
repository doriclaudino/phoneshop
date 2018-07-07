from django.contrib import admin
from django import forms
from .models import Supplier


class SupplierAdminForm(forms.ModelForm):

    class Meta:
        model = Supplier
        fields = '__all__'


class SupplierAdmin(admin.ModelAdmin):
    form = SupplierAdminForm
    list_display = ['name', 'slug', 'created_at', 'updated_at', 'website']
    readonly_fields = ['slug', 'created_at', 'updated_at', 'website']


admin.site.register(Supplier, SupplierAdmin)
