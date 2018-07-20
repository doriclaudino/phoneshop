from django import forms
from .models import CostType, Cost


class CostTypeForm(forms.ModelForm):
    class Meta:
        model = CostType
        fields = ['name']


class CostForm(forms.ModelForm):
    class Meta:
        model = Cost
        fields = ['type', 'amount', 'details']
