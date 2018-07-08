from django import forms
from .models import Supplier, PurchaseOrderStatus


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'website']


class PurchaseOrderStatusForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrderStatus
        fields = ['name']


