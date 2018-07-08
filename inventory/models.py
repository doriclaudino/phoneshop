from django.core.urlresolvers import reverse
from django_extensions.db.fields import AutoSlugField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields
from django.utils.translation import gettext_lazy as _
from catalog.models import ProductModel
from purchase.models import PurchaseOrderItem


class IdentifierType(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    update_at = models.DateTimeField(auto_now=True, editable=False)
    objects = models.Manager()

    class Meta:
        ordering = ('-pk',)
        verbose_name_plural = _('Identifier Types')
        verbose_name = _('Identifier Type')

    def __str__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('inventory_identifiertype_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('inventory_identifiertype_update', args=(self.slug,))


class LocationType(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    objects = models.Manager()

    class Meta:
        ordering = ('-pk',)
        verbose_name_plural = _('Location Types')
        verbose_name = _('Location Type')

    def __str__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('inventory_locationtype_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('inventory_locationtype_update', args=(self.slug,))


class Location(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    objects = models.Manager()

    # Relationship Fields
    type = models.ForeignKey(
        LocationType, related_name='+', on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('-pk',)
        verbose_name_plural = _('Locations')
        verbose_name = _('Location')

    def __str__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('inventory_location_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('inventory_location_update', args=(self.slug,))


class Identifier(models.Model):

    # Fields
    value = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(
        populate_from=['type', 'value'], blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    objects = models.Manager()

    # Relationship Fields
    type = models.ForeignKey(IdentifierType, related_name='+')

    class Meta:
        ordering = ('-pk',)
        verbose_name_plural = _('Identifiers')
        verbose_name = _('Identifier')

    def __str__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('inventory_identifier_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('inventory_identifier_update', args=(self.slug,))


class Item(models.Model):

    # Fields
    slug = extension_fields.AutoSlugField(
        populate_from=['product', 'identifier'], blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    objects = models.Manager()

    # Relationship Fields
    product = models.ForeignKey(PurchaseOrderItem, related_name='+')
    identifier = models.ForeignKey(Identifier, related_name='+')
    location = models.ForeignKey(Location, related_name='+')

    class Meta:
        ordering = ('-pk',)
        verbose_name_plural = _('Items')
        verbose_name = _('Item')

    def __str__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('inventory_item_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('inventory_item_update', args=(self.slug,))
