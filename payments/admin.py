from django.contrib import admin
from django import forms
from .models import PaymentMethod, PaymentStatus, Payment


class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(PaymentMethod, PaymentMethodAdmin)


class PaymentStatusAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(PaymentStatus, PaymentStatusAdmin)


class PaymentAdmin(admin.ModelAdmin):
    list_display = ['slug', 'payment_of', 'date',
                    'amount', 'created_at', 'updated_at', ]
    readonly_fields = ['slug',  'date', 'amount', 'created_at', 'updated_at']


admin.site.register(Payment, PaymentAdmin)
