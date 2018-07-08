from django import forms
from .models import Supplier, PurchaseOrderStatus, PurchaseOrder, PurchaseOrderItem


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'website']


class PurchaseOrderStatusForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrderStatus
        fields = ['name']


class PurchaseOrderForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrder
        fields = ['details', 'supplier', 'status', 'tracking']


class PurchaseOrderItemForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrderItem
        fields = ['quantity', 'price', 'product', 'order']
