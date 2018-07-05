from django import forms
from .models import Location, Carrier, TrackingStatus, Tracking


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name']


class CarrierForm(forms.ModelForm):
    class Meta:
        model = Carrier
        fields = ['name', 'website', 'tracking_url']


class TrackingStatusForm(forms.ModelForm):
    class Meta:
        model = TrackingStatus
        fields = ['name']


class TrackingForm(forms.ModelForm):
    class Meta:
        model = Tracking
        fields = ['carrier', 'number', 'description', 'status', 'previous']


