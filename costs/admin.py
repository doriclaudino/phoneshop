from django.contrib import admin
from django import forms
from .models import CostType, PurchaseCost, ItemCost, SellCost, TrackingCost
from payments.models import SellCostPayment, PurchaseCostPayment, ItemCostPayment, TrackingCostPayment


class CostAdmin(admin.ModelAdmin):
    fields = ['ref', 'type', 'amount', 'details']
    list_display = ['slug', 'ref', 'type',
                    'amount', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


class tabular(admin.TabularInline):
    extra = 1


class CostTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(CostType, CostTypeAdmin)


class InlinePurchaseCostPayment(tabular):
    model = PurchaseCostPayment


class PurchaseCostAdmin(CostAdmin):
    inlines = [InlinePurchaseCostPayment]


admin.site.register(PurchaseCost, PurchaseCostAdmin)


class InlineItemCostPayment(tabular):
    model = ItemCostPayment


class ItemCostAdmin(CostAdmin):
    inlines = [InlineItemCostPayment, ]


admin.site.register(ItemCost, ItemCostAdmin)


class InlineSellCostPayment(tabular):
    model = SellCostPayment


class SellCostAdmin(CostAdmin):
    inlines = [InlineSellCostPayment, ]


admin.site.register(SellCost, SellCostAdmin)


class InlineTrackingCostPayment(tabular):
    model = TrackingCostPayment


class TrackingCostAdmin(CostAdmin):
    inlines = [InlineTrackingCostPayment, ]


admin.site.register(TrackingCost, TrackingCostAdmin)
