from django import forms
from .models import Brand, Model


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name']


class ModelForm(forms.ModelForm):
    class Meta:
        model = Model
        fields = ['name']
