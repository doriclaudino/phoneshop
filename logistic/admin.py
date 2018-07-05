from django.contrib import admin
from django import forms
from .models import Location, Carrier, TrackingStatus, Tracking


class LocationAdminForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = '__all__'


class LocationAdmin(admin.ModelAdmin):
    form = LocationAdminForm
    list_display = ['name', 'slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(Location, LocationAdmin)


class CarrierAdminForm(forms.ModelForm):

    class Meta:
        model = Carrier
        fields = '__all__'


class CarrierAdmin(admin.ModelAdmin):
    form = CarrierAdminForm
    list_display = ['name', 'website', 'tracking_url',
                    'slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at']


admin.site.register(Carrier, CarrierAdmin)


class TrackingStatusAdminForm(forms.ModelForm):

    class Meta:
        model = TrackingStatus
        fields = '__all__'


class TrackingStatusAdmin(admin.ModelAdmin):
    form = TrackingStatusAdminForm
    list_display = ['name', 'slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(TrackingStatus, TrackingStatusAdmin)


class TrackingAdminForm(forms.ModelForm):

    class Meta:
        model = Tracking
        fields = '__all__'


class TrackingAdmin(admin.ModelAdmin):
    form = TrackingAdminForm
    fields = ['carrier', 'number', 'status',
              'description', 'slug', 'created_at', 'updated_at']
    list_display = ['slug', 'carrier', 'number', 'status',
                    'description', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(Tracking, TrackingAdmin)
