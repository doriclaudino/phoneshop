from django.contrib import admin
from django import forms
from .models import CostType, Cost


class CostTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(CostType, CostTypeAdmin)


class CostAdmin(admin.ModelAdmin):
    fields = ['type', 'payment', 'details']
    list_display = ['slug', 'cost_of', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(Cost, CostAdmin)
