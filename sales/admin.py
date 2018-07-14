from django.contrib import admin
from django import forms
from .models import Seller, SellOrderStatus, SellOrder, SellOrderItem
from costs.models import SellCost

class SellerAdminForm(forms.ModelForm):

    class Meta:
        model = Seller
        fields = '__all__'


class SellerAdmin(admin.ModelAdmin):
    form = SellerAdminForm
    list_display = ['name', 'slug', 'created_at', 'updated_at', 'website']
    readonly_fields = ['slug', 'created_at', 'updated_at', 'website']


admin.site.register(Seller, SellerAdmin)


class SellOrderStatusAdminForm(forms.ModelForm):

    class Meta:
        model = SellOrderStatus
        fields = '__all__'


class SellOrderStatusAdmin(admin.ModelAdmin):
    form = SellOrderStatusAdminForm
    list_display = ['name', 'slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(SellOrderStatus, SellOrderStatusAdmin)


class InlineOrderItem(admin.TabularInline):
    model = SellOrderItem
    fields = ['order', 'product', 'quantity', 'price']
    list_display_links = ['product']


class InlineOrderItemCost(admin.TabularInline):
    model = SellCost
    fields = ['type', 'details', 'payment']


class SellOrderAdminForm(forms.ModelForm):

    class Meta:
        model = SellOrder
        fields = '__all__'


class SellOrderAdmin(admin.ModelAdmin):
    form = SellOrderAdminForm
    list_display = ['slug', 'details', 'created_at', 'updated_at']
    fields = ['seller', 'status', 'tracking', 'details']
    readonly_fields = ['slug', 'created_at', 'updated_at']
    inlines = [InlineOrderItem, InlineOrderItemCost]


admin.site.register(SellOrder, SellOrderAdmin)


class SellOrderItemAdminForm(forms.ModelForm):

    class Meta:
        model = SellOrderItem
        fields = '__all__'


class SellOrderItemAdmin(admin.ModelAdmin):
    form = SellOrderItemAdminForm
    fields = ['order', 'product', 'quantity',
              'price', 'slug', 'created_at', 'updated_at']
    list_display = ['slug', 'order', 'product',
                    'created_at', 'updated_at', 'quantity', 'price']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(SellOrderItem, SellOrderItemAdmin)
