from django.contrib import admin
from django import forms
from .models import CostType, Cost
from payments.models import Payment
from django.contrib.contenttypes.admin import GenericTabularInline


class CostTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(CostType, CostTypeAdmin)


class InlinePayment(GenericTabularInline):
    model = Payment
    extra = 1


class CostAdmin(admin.ModelAdmin):
    fields = ['type', 'amount', 'details', 'content_type']
    list_display = ['slug', 'amount',
                    'content_type', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at', 'content_type']
    inlines = [InlinePayment, ]


admin.site.register(Cost, CostAdmin)
