from django import forms
from .models import PaymentType, PaymentStatus, Payment, OrderPayments


class PaymentTypeForm(forms.ModelForm):
    class Meta:
        model = PaymentType
        fields = ['name']


class PaymentStatusForm(forms.ModelForm):
    class Meta:
        model = PaymentStatus
        fields = ['name']


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount', 'status', 'type']


class OrderPaymentsForm(forms.ModelForm):
    class Meta:
        model = OrderPayments
        fields = ['order', 'payment']
