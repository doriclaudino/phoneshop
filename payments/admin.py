from django.contrib import admin
from django import forms
from .models import PaymentType, PaymentStatus, Payment, OrderPayments


class PaymentTypeAdminForm(forms.ModelForm):

    class Meta:
        model = PaymentType
        fields = '__all__'


class PaymentTypeAdmin(admin.ModelAdmin):
    form = PaymentTypeAdminForm
    list_display = ['name', 'slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(PaymentType, PaymentTypeAdmin)


class PaymentStatusAdminForm(forms.ModelForm):

    class Meta:
        model = PaymentStatus
        fields = '__all__'


class PaymentStatusAdmin(admin.ModelAdmin):
    form = PaymentStatusAdminForm
    list_display = ['name', 'slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(PaymentStatus, PaymentStatusAdmin)


class PaymentAdminForm(forms.ModelForm):

    class Meta:
        model = Payment
        fields = '__all__'


class PaymentAdmin(admin.ModelAdmin):
    form = PaymentAdminForm
    fields = ['type', 'status', 'amount', 'date',
              'slug', 'created_at', 'updated_at', ]
    list_display = ['slug', 'type', 'status',
                    'amount', 'date', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(Payment, PaymentAdmin)


class OrderPaymentsAdminForm(forms.ModelForm):

    class Meta:
        model = OrderPayments
        fields = '__all__'


class OrderPaymentsAdmin(admin.ModelAdmin):
    form = OrderPaymentsAdminForm
    list_display = ['order', 'payment',
                    'slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(OrderPayments, OrderPaymentsAdmin)
