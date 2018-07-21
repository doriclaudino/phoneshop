from django.contrib import admin
from django import forms
from .models import SellOrderStatus, SellOrder, SellOrderItem, Customer
from costs.models import Cost
from payments.models import Payment
from django.contrib.contenttypes.admin import GenericTabularInline


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['slug',  'name', 'user', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(Customer, CustomerAdmin)


class SellOrderStatusAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(SellOrderStatus, SellOrderStatusAdmin)


class InlineOrderItem(admin.TabularInline):
    model = SellOrderItem
    fields = ['order', 'product', 'quantity', 'price']
    extra = 1


class InlinePayment(GenericTabularInline):
    model = Payment
    fields = ['method', 'amount', 'status', 'date']
    extra = 1


class InlineCost(GenericTabularInline):
    model = Cost
    fields = ['amount', 'details', 'type']
    extra = 1


class SellOrderAdmin(admin.ModelAdmin):
    list_display = ['slug', 'seller', 'status',
                    'customer', 'tracking', 'created_at', 'updated_at']
    fields = ['seller', 'status',  'customer', 'tracking', 'details']
    readonly_fields = ['slug', 'created_at', 'updated_at']
    inlines = [InlineOrderItem, InlinePayment, InlineCost]


admin.site.register(SellOrder, SellOrderAdmin)


class SellOrderItemAdmin(admin.ModelAdmin):
    fields = ['order', 'product', 'quantity',
              'price', 'slug', 'created_at', 'updated_at']
    list_display = ['slug', 'order', 'product',
                    'created_at', 'updated_at', 'quantity', 'price']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(SellOrderItem, SellOrderItemAdmin)
