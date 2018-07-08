from django.contrib import admin
from django import forms
from .models import Supplier, PurchaseOrderStatus, PurchaseOrder, PurchaseOrderItem


class SupplierAdminForm(forms.ModelForm):

    class Meta:
        model = Supplier
        fields = '__all__'


class SupplierAdmin(admin.ModelAdmin):
    form = SupplierAdminForm
    list_display = ['name', 'slug', 'created_at', 'updated_at', 'website']
    readonly_fields = ['slug', 'created_at', 'updated_at', 'website']


admin.site.register(Supplier, SupplierAdmin)


class PurchaseOrderStatusAdminForm(forms.ModelForm):

    class Meta:
        model = PurchaseOrderStatus
        fields = '__all__'


class PurchaseOrderStatusAdmin(admin.ModelAdmin):
    form = PurchaseOrderStatusAdminForm
    list_display = ['name', 'slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(PurchaseOrderStatus, PurchaseOrderStatusAdmin)


class PurchaseOrderAdminForm(forms.ModelForm):

    class Meta:
        model = PurchaseOrder
        fields = '__all__'


class PurchaseOrderAdmin(admin.ModelAdmin):
    form = PurchaseOrderAdminForm
    list_display = ['slug', 'details', 'created_at', 'updated_at']
    fields = ['supplier', 'status', 'tracking',
              'details', 'slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(PurchaseOrder, PurchaseOrderAdmin)


class PurchaseOrderItemAdminForm(forms.ModelForm):

    class Meta:
        model = PurchaseOrderItem
        fields = '__all__'


class PurchaseOrderItemAdmin(admin.ModelAdmin):
    form = PurchaseOrderItemAdminForm
    fields = ['order', 'product', 'quantity',
              'price', 'slug', 'created_at', 'updated_at']
    list_display = ['slug', 'order', 'product',
                    'created_at', 'updated_at', 'quantity', 'price']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(PurchaseOrderItem, PurchaseOrderItemAdmin)
