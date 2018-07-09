from django.contrib import admin
from django import forms
from .models import IdentifierType, LocalType, Local, Identifier, Item


class IdentifierTypeAdminForm(forms.ModelForm):

    class Meta:
        model = IdentifierType
        fields = '__all__'


class IdentifierTypeAdmin(admin.ModelAdmin):
    form = IdentifierTypeAdminForm
    list_display = ['name', 'slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(IdentifierType, IdentifierTypeAdmin)


class LocalTypeAdminForm(forms.ModelForm):

    class Meta:
        model = LocalType
        fields = '__all__'


class LocalTypeAdmin(admin.ModelAdmin):
    form = LocalTypeAdminForm
    list_display = ['name', 'slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(LocalType, LocalTypeAdmin)


class LocalAdminForm(forms.ModelForm):

    class Meta:
        model = Local
        fields = '__all__'


class LocalAdmin(admin.ModelAdmin):
    form = LocalAdminForm
    list_display = ['name', 'slug', 'created_at', 'updated_at']
    fields = ['type', 'name', 'slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(Local, LocalAdmin)


class IdentifierAdminForm(forms.ModelForm):

    class Meta:
        model = Identifier
        fields = '__all__'


class IdentifierAdmin(admin.ModelAdmin):
    form = IdentifierAdminForm
    list_display = ['value', 'slug', 'created_at', 'updated_at']
    fields = ['type', 'value', 'slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(Identifier, IdentifierAdmin)


class ItemAdminForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = '__all__'


class ItemAdmin(admin.ModelAdmin):
    form = ItemAdminForm
    list_display = ['slug', 'product', 'local',
                    'identifier', 'created_at', 'updated_at']
    fields = ['product', 'local', 'identifier',
              'slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(Item, ItemAdmin)
