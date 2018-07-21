from django.contrib import admin
from django import forms
from .models import PurchaseOrderStatus, PurchaseOrder, PurchaseOrderItem, Supplier
from costs.models import Cost
from payments.models import Payment
from django.contrib.contenttypes.admin import GenericTabularInline


class SupplierAdmin(admin.ModelAdmin):
    list_display = ['slug', 'name', 'user',
                    'website', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(Supplier, SupplierAdmin)


class PurchaseOrderStatusAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(PurchaseOrderStatus, PurchaseOrderStatusAdmin)


class InlineOrderItem(admin.TabularInline):
    model = PurchaseOrderItem
    fields = ['order', 'product', 'quantity', 'price']
    list_display_links = ['product']
    extra = 1


class InlinePayment(GenericTabularInline):
    model = Payment
    fields = ['method', 'amount', 'status', 'date']
    extra = 1


class InlineCost(GenericTabularInline):
    model = Cost
    fields = ['amount', 'details', 'type']
    extra = 1


class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ['slug', 'details', 'created_at', 'updated_at']
    fields = ['supplier', 'status', 'tracking', 'details']
    readonly_fields = ['slug', 'created_at', 'updated_at']
    inlines = [InlineOrderItem, InlinePayment, InlineCost]


admin.site.register(PurchaseOrder, PurchaseOrderAdmin)


class PurchaseOrderItemAdmin(admin.ModelAdmin):
    fields = ['order', 'product', 'quantity',
              'price', 'slug', 'created_at', 'updated_at']
    list_display = ['slug', 'order', 'product',
                    'created_at', 'updated_at', 'quantity', 'price']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(PurchaseOrderItem, PurchaseOrderItemAdmin)
