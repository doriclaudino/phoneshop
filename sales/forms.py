from django import forms
from .models import Customer, SellOrderStatus, SellOrder, SellOrderItem


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name']


class SellOrderStatusForm(forms.ModelForm):
    class Meta:
        model = SellOrderStatus
        fields = ['name']


class SellOrderForm(forms.ModelForm):
    class Meta:
        model = SellOrder
        fields = ['details', 'seller', 'status', 'tracking']


class SellOrderItemForm(forms.ModelForm):
    class Meta:
        model = SellOrderItem
        fields = ['quantity', 'price', 'product', 'order']
