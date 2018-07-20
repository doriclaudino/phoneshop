from django import forms
from .models import Carrier, TrackingStatus, Tracking


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
