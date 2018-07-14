from django import forms
from .models import CostType, Cost, PurchaseCosts, SellCosts, ItemCosts, TrackingCosts


class CostTypeForm(forms.ModelForm):
    class Meta:
        model = CostType
        fields = ['name']


class CostForm(forms.ModelForm):
    class Meta:
        model = Cost
        fields = ['details', 'type', 'payment']


class PurchaseCostsForm(forms.ModelForm):
    class Meta:
        model = PurchaseCosts
        fields = []


class SellCostsForm(forms.ModelForm):
    class Meta:
        model = SellCosts
        fields = ['ref', 'cost']


class ItemCostsForm(forms.ModelForm):
    class Meta:
        model = ItemCosts
        fields = ['ref', 'cost']


class TrackingCostsForm(forms.ModelForm):
    class Meta:
        model = TrackingCosts
        fields = ['ref', 'cost']
