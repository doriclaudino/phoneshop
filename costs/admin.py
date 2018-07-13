from django.contrib import admin
from django import forms
from .models import CostType, Cost, PurchaseCosts, SellCosts, ItemCosts


class CostTypeAdminForm(forms.ModelForm):

    class Meta:
        model = CostType
        fields = '__all__'


class CostTypeAdmin(admin.ModelAdmin):
    form = CostTypeAdminForm
    list_display = ['name', 'slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(CostType, CostTypeAdmin)


class CostAdminForm(forms.ModelForm):

    class Meta:
        model = Cost
        fields = '__all__'


class CostAdmin(admin.ModelAdmin):
    form = CostAdminForm
    fields = ['type', 'payment', 'details', 'slug', 'created_at', 'updated_at']
    list_display = ['slug', 'created_at', 'updated_at', 'details']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(Cost, CostAdmin)


class PurchaseCostsAdminForm(forms.ModelForm):

    class Meta:
        model = PurchaseCosts
        fields = '__all__'


class PurchaseCostsAdmin(admin.ModelAdmin):
    form = PurchaseCostsAdminForm
    list_display = ['slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(PurchaseCosts, PurchaseCostsAdmin)


class SellCostsAdminForm(forms.ModelForm):

    class Meta:
        model = SellCosts
        fields = '__all__'


class SellCostsAdmin(admin.ModelAdmin):
    form = SellCostsAdminForm
    list_display = ['slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(SellCosts, SellCostsAdmin)


class ItemCostsAdminForm(forms.ModelForm):

    class Meta:
        model = ItemCosts
        fields = '__all__'


class ItemCostsAdmin(admin.ModelAdmin):
    form = ItemCostsAdminForm
    list_display = ['slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(ItemCosts, ItemCostsAdmin)
