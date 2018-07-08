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
from logistic.models import Tracking


class Supplier(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    website = models.TextField(max_length=100)
    objects = models.Manager()

    class Meta:
        ordering = ('-pk',)
        verbose_name_plural = _('Suppliers')
        verbose_name = _('Supplier')

    def __str__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('purchase_supplier_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('purchase_supplier_update', args=(self.slug,))


class PurchaseOrderStatus(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    objects = models.Manager()

    class Meta:
        ordering = ('-pk',)
        verbose_name_plural = _('Purchase Order Statuses')
        verbose_name = _('Purchase Order Status')

    def __str__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('purchase_purchaseorderstatus_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('purchase_purchaseorderstatus_update', args=(self.slug,))


class PurchaseOrder(models.Model):

    # Fields
    details = models.TextField(max_length=500, blank=True)
    slug = extension_fields.AutoSlugField(
        populate_from=['supplier', 'tracking'], blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    objects = models.Manager()

    # Relationship Fields
    supplier = models.ForeignKey(Supplier, related_name='+')
    status = models.ForeignKey(PurchaseOrderStatus, related_name='+')
    tracking = models.ForeignKey(Tracking, related_name='+', blank=True)

    class Meta:
        ordering = ('-pk',)
        verbose_name_plural = _('Purchase Orders')
        verbose_name = _('Purchase Order')

    def __str__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('purchase_purchaseorder_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('purchase_purchaseorder_update', args=(self.slug,))
