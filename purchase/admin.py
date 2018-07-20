from django.contrib import admin
from django import forms
from .models import Supplier, PurchaseOrderStatus, PurchaseOrder, PurchaseOrderItem
from costs.models import Cost
from django.contrib.contenttypes.admin import GenericTabularInline


class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at', 'updated_at', 'website']
    readonly_fields = ['slug', 'created_at', 'updated_at', 'website']


admin.site.register(Supplier, SupplierAdmin)


class PurchaseOrderStatusAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(PurchaseOrderStatus, PurchaseOrderStatusAdmin)


class InlineOrderItem(admin.TabularInline):
    model = PurchaseOrderItem
    fields = ['order', 'product', 'quantity', 'price']
    list_display_links = ['product']


class InlineOrderItemCost(GenericTabularInline):
    model = Cost
    fields = ['type', 'details', 'payment']


class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ['slug', 'details', 'created_at', 'updated_at']
    fields = ['supplier', 'status', 'tracking', 'details']
    readonly_fields = ['slug', 'created_at', 'updated_at']
    inlines = [InlineOrderItem, InlineOrderItemCost]


admin.site.register(PurchaseOrder, PurchaseOrderAdmin)


class PurchaseOrderItemAdmin(admin.ModelAdmin):
    fields = ['order', 'product', 'quantity',
              'price', 'slug', 'created_at', 'updated_at']
    list_display = ['slug', 'order', 'product',
                    'created_at', 'updated_at', 'quantity', 'price']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(PurchaseOrderItem, PurchaseOrderItemAdmin)
