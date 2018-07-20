from django.contrib import admin
from django import forms
from .models import Location, Carrier, TrackingStatus, Tracking
from django.contrib.contenttypes.admin import GenericTabularInline
from costs.models import Cost


class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(Location, LocationAdmin)


class CarrierAdmin(admin.ModelAdmin):
    list_display = ['name', 'website', 'tracking_url',
                    'slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at']


admin.site.register(Carrier, CarrierAdmin)


class TrackingStatusAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(TrackingStatus, TrackingStatusAdmin)


class InlineTrackingCost(GenericTabularInline):
    model = Cost
    fields = ['type',  'details', 'payment']
    extra = 1


class TrackingAdmin(admin.ModelAdmin):
    fields = ['carrier', 'number', 'status',
              'description', 'slug', 'created_at', 'updated_at']
    list_display = ['slug', 'carrier', 'number', 'status',
                    'description', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']
    inlines = [InlineTrackingCost, ]


admin.site.register(Tracking, TrackingAdmin)
