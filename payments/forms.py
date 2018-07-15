from django import forms
from .models import PaymentMethod, PaymentStatus, SalePayment, PurchasePayment, TrackingPayment


class PaymentMethodForm(forms.ModelForm):
    class Meta:
        model = PaymentMethod
        fields = ['name']


class PaymentStatusForm(forms.ModelForm):
    class Meta:
        model = PaymentStatus
        fields = ['name']


class SalePaymentForm(forms.ModelForm):
    class Meta:
        model = SalePayment
        fields = ['date', 'amount', 'status', 'method', 'ref']


class PurchasePaymentForm(forms.ModelForm):
    class Meta:
        model = PurchasePayment
        fields = ['date', 'amount', 'status', 'method', 'ref']


class TrackingPaymentForm(forms.ModelForm):
    class Meta:
        model = TrackingPayment
        fields = ['date', 'amount', 'status', 'method', 'ref']
