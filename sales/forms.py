from django import forms
from .models import Seller, SellOrderStatus, SellOrder, SellOrderItem


class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['name', 'website']


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


