from django.contrib import admin
from django import forms
from .models import Carrier, TrackingStatus, Tracking
from django.contrib.contenttypes.admin import GenericTabularInline
from costs.models import Cost
from django.contrib.contenttypes.admin import GenericTabularInline


class CarrierAdmin(admin.ModelAdmin):
    list_display = ['name', 'website', 'tracking_url',
                    'slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at']


admin.site.register(Carrier, CarrierAdmin)


class TrackingStatusAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(TrackingStatus, TrackingStatusAdmin)


class InlineCost(GenericTabularInline):
    model = Cost
    fields = ['type', 'amount', 'details']
    extra = 1


class TrackingAdmin(admin.ModelAdmin):
    fields = ['carrier', 'number', 'status',
              'description', 'slug', 'created_at', 'updated_at']
    list_display = ['slug', 'carrier', 'number', 'status',
                    'description', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']
    inlines = [InlineCost, ]


admin.site.register(Tracking, TrackingAdmin)
