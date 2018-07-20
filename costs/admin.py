from django.contrib import admin
from django import forms
from .models import CostType, Cost
from payments.models import Payment
from django.contrib.contenttypes.admin import GenericTabularInline


class CostTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(CostType, CostTypeAdmin)


class InlineCostPayment(GenericTabularInline):
    model = Payment
    extra = 1


class CostAdmin(admin.ModelAdmin):
    fields = ['type', 'details']
    list_display = ['slug', 'cost_of', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']
    inlines = [InlineCostPayment, ]


admin.site.register(Cost, CostAdmin)
