from django.contrib import admin
from django import forms
from .models import IdentifierType, LocationType, Location, Identifier, Item


class IdentifierTypeAdminForm(forms.ModelForm):

    class Meta:
        model = IdentifierType
        fields = '__all__'


class IdentifierTypeAdmin(admin.ModelAdmin):
    form = IdentifierTypeAdminForm
    list_display = ['name', 'slug', 'created_at', 'update_at']
    readonly_fields = ['slug', 'created_at', 'update_at']


admin.site.register(IdentifierType, IdentifierTypeAdmin)


class LocationTypeAdminForm(forms.ModelForm):

    class Meta:
        model = LocationType
        fields = '__all__'


class LocationTypeAdmin(admin.ModelAdmin):
    form = LocationTypeAdminForm
    list_display = ['name', 'slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(LocationType, LocationTypeAdmin)


class LocationAdminForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = '__all__'


class LocationAdmin(admin.ModelAdmin):
    form = LocationAdminForm
    list_display = ['name', 'slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(Location, LocationAdmin)


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
    list_display = ['slug', 'product', 'location',
                    'identifier', 'created_at', 'updated_at']
    fields = ['product', 'location', 'identifier',
              'slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(Item, ItemAdmin)
