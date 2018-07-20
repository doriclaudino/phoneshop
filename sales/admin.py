from django.contrib import admin
from django import forms
from .models import Seller, SellOrderStatus, SellOrder, SellOrderItem
from costs.models import Cost
from payments.models import Payment
from django.contrib.contenttypes.admin import GenericTabularInline


class SellerAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at', 'updated_at', 'website']
    readonly_fields = ['slug', 'created_at', 'updated_at', 'website']


admin.site.register(Seller, SellerAdmin)


class SellOrderStatusAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(SellOrderStatus, SellOrderStatusAdmin)


class InlineOrderItem(admin.TabularInline):
    model = SellOrderItem
    fields = ['order', 'product', 'quantity', 'price']
    list_display_links = ['product']


class SellOrderAdmin(admin.ModelAdmin):
    list_display = ['slug', 'details', 'created_at', 'updated_at']
    fields = ['seller', 'status', 'tracking', 'details']
    readonly_fields = ['slug', 'created_at', 'updated_at']
    inlines = [InlineOrderItem, ]


admin.site.register(SellOrder, SellOrderAdmin)


class SellOrderItemAdmin(admin.ModelAdmin):
    fields = ['order', 'product', 'quantity',
              'price', 'slug', 'created_at', 'updated_at']
    list_display = ['slug', 'order', 'product',
                    'created_at', 'updated_at', 'quantity', 'price']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(SellOrderItem, SellOrderItemAdmin)
