from django.contrib import admin
from django import forms
from .models import CostType, PurchaseCost, ItemCost, SellCost, TrackingCost
from payments.models import SellCostPayment, PurchaseCostPayment


class CostTypeAdminForm(forms.ModelForm):

    class Meta:
        model = CostType
        fields = '__all__'


class CostTypeAdmin(admin.ModelAdmin):
    form = CostTypeAdminForm
    list_display = ['name']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(CostType, CostTypeAdmin)


class InlinePurchaseCostPayment(admin.TabularInline):
    model = PurchaseCostPayment
    extra = 1


class PurchaseCostAdminForm(forms.ModelForm):

    class Meta:
        model = PurchaseCost
        fields = '__all__'


class PurchaseCostAdmin(admin.ModelAdmin):
    form = PurchaseCostAdminForm
    fields = ['ref', 'type', 'details']
    list_display = ['slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']
    inlines = [InlinePurchaseCostPayment]


admin.site.register(PurchaseCost, PurchaseCostAdmin)


class ItemCostAdminForm(forms.ModelForm):

    class Meta:
        model = ItemCost
        fields = '__all__'


class ItemCostAdmin(admin.ModelAdmin):
    form = ItemCostAdminForm
    fields = ['ref', 'type', 'details']
    list_display = ['slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(ItemCost, ItemCostAdmin)


class SellCostAdminForm(forms.ModelForm):

    class Meta:
        model = SellCost
        fields = '__all__'


class InlineSellCostPayment(admin.TabularInline):
    model = SellCostPayment
    extra = 1


class SellCostAdmin(admin.ModelAdmin):
    form = SellCostAdminForm
    fields = ['ref', 'type', 'details']
    list_display = ['slug', 'ref', 'type',
                    'details', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']
    inlines = [InlineSellCostPayment, ]


admin.site.register(SellCost, SellCostAdmin)


class TrackingCostAdminForm(forms.ModelForm):

    class Meta:
        model = TrackingCost
        fields = '__all__'


class TrackingCostAdmin(admin.ModelAdmin):
    form = TrackingCostAdminForm
    fields = ['ref', 'type', 'details']
    list_display = ['slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(TrackingCost, TrackingCostAdmin)
