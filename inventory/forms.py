from django import forms
from .models import IdentifierType, LocalType, Local, Identifier, Item


class IdentifierTypeForm(forms.ModelForm):
    class Meta:
        model = IdentifierType
        fields = ['name']


class LocalTypeForm(forms.ModelForm):
    class Meta:
        model = LocalType
        fields = ['name']


class LocalForm(forms.ModelForm):
    class Meta:
        model = Local
        fields = ['name', 'type']


class IdentifierForm(forms.ModelForm):
    class Meta:
        model = Identifier
        fields = ['value', 'type']


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['identifier', 'product', 'local']


