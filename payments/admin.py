from django.contrib import admin
from django import forms
from .models import PaymentMethod, PaymentStatus, SalePayment, PurchasePayment, TrackingPayment
from .models import PurchaseCostPayment,  SellCostPayment,  ItemCostPayment, TrackingCostPayment


class PaymentMethodAdminForm(forms.ModelForm):

    class Meta:
        model = PaymentMethod
        fields = '__all__'


class PaymentMethodAdmin(admin.ModelAdmin):
    form = PaymentMethodAdminForm
    list_display = ['name', 'slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(PaymentMethod, PaymentMethodAdmin)


class PaymentStatusAdminForm(forms.ModelForm):

    class Meta:
        model = PaymentStatus
        fields = '__all__'


class PaymentStatusAdmin(admin.ModelAdmin):
    form = PaymentStatusAdminForm
    list_display = ['name', 'slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(PaymentStatus, PaymentStatusAdmin)


class SalePaymentAdminForm(forms.ModelForm):

    class Meta:
        model = SalePayment
        fields = '__all__'


class SalePaymentAdmin(admin.ModelAdmin):
    form = SalePaymentAdminForm
    list_display = ['slug', 'created_at', 'updated_at', 'date', 'amount']
    readonly_fields = ['slug', 'created_at', 'updated_at', 'date', 'amount']


admin.site.register(SalePayment, SalePaymentAdmin)


class PurchasePaymentAdminForm(forms.ModelForm):

    class Meta:
        model = PurchasePayment
        fields = '__all__'


class PurchasePaymentAdmin(admin.ModelAdmin):
    form = PurchasePaymentAdminForm
    list_display = ['slug', 'created_at', 'updated_at', 'date', 'amount']
    readonly_fields = ['slug', 'created_at', 'updated_at', 'date', 'amount']


admin.site.register(PurchasePayment, PurchasePaymentAdmin)


class TrackingPaymentAdminForm(forms.ModelForm):

    class Meta:
        model = TrackingPayment
        fields = '__all__'


class TrackingPaymentAdmin(admin.ModelAdmin):
    form = TrackingPaymentAdminForm
    list_display = ['slug', 'created_at', 'updated_at', 'date', 'amount']
    readonly_fields = ['slug', 'created_at', 'updated_at', 'date', 'amount']


admin.site.register(TrackingPayment, TrackingPaymentAdmin)


admin.site.register(PurchaseCostPayment)
admin.site.register(SellCostPayment)
admin.site.register(ItemCostPayment)
admin.site.register(TrackingCostPayment)
