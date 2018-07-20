from django import forms
from .models import PaymentMethod, PaymentStatus, Payment


class PaymentMethodForm(forms.ModelForm):
    class Meta:
        model = PaymentMethod
        fields = ['name']


class PaymentStatusForm(forms.ModelForm):
    class Meta:
        model = PaymentStatus
        fields = ['name']


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['date', 'amount', 'status', 'method']
