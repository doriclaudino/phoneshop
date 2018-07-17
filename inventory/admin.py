from django.contrib import admin
from django import forms
from .models import IdentifierType, LocalType, Local, Identifier, Item


class IdentifierTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(IdentifierType, IdentifierTypeAdmin)


class LocalTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(LocalType, LocalTypeAdmin)


class LocalAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at', 'updated_at']
    fields = ['type', 'name', 'slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(Local, LocalAdmin)


class IdentifierAdmin(admin.ModelAdmin):
    list_display = ['value', 'slug', 'created_at', 'updated_at']
    fields = ['type', 'value', 'slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(Identifier, IdentifierAdmin)


class ItemAdmin(admin.ModelAdmin):
    list_display = ['slug', 'product', 'local',
                    'identifier', 'created_at', 'updated_at']
    fields = ['product', 'local', 'identifier',
              'slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(Item, ItemAdmin)
