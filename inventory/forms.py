from django import forms
from .models import IdentifierType, LocationType, Location, Identifier, Item


class IdentifierTypeForm(forms.ModelForm):
    class Meta:
        model = IdentifierType
        fields = ['name']


class LocationTypeForm(forms.ModelForm):
    class Meta:
        model = LocationType
        fields = ['name']


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'type']


class IdentifierForm(forms.ModelForm):
    class Meta:
        model = Identifier
        fields = ['value', 'type']


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['identifier', 'product',  'location']
