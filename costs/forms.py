from django import forms
from .models import CostType, PurchaseCost, ItemCost, SellCost, TrackingCost


class CostTypeForm(forms.ModelForm):
    class Meta:
        model = CostType
        fields = ['name']


class PurchaseCostForm(forms.ModelForm):
    class Meta:
        model = PurchaseCost
        fields = ['ref', 'type']


class ItemCostForm(forms.ModelForm):
    class Meta:
        model = ItemCost
        fields = ['ref', 'type']


class SellCostForm(forms.ModelForm):
    class Meta:
        model = SellCost
        fields = ['ref', 'type']


class TrackingCostForm(forms.ModelForm):
    class Meta:
        model = TrackingCost
        fields = ['ref', 'type']
