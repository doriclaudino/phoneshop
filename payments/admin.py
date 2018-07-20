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
    fields = ['date', 'amount', 'content_type', ]
    list_display = ['slug', 'content_type', 'date',
                    'amount', 'created_at', 'updated_at', ]
    readonly_fields = ['slug', 'content_type', 'created_at', 'updated_at']


admin.site.register(Payment, PaymentAdmin)
