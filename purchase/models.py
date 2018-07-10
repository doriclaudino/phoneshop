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
from catalog.models import ProductModel


class Supplier(models.Model):

    # Fields
    name = models.CharField(max_length=255, unique=True)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    website = models.CharField(max_length=100)
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
    name = models.CharField(max_length=255, unique=True)
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
        unique_together = ('supplier', 'tracking')

    def __str__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('purchase_purchaseorder_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('purchase_purchaseorder_update', args=(self.slug,))


class PurchaseOrderItem(models.Model):

    # Fields
    slug = extension_fields.AutoSlugField(
        populate_from=['product', 'order', 'quantity', 'price'], blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, default=100.00)
    objects = models.Manager()

    # Relationship Fields
    product = models.ForeignKey(ProductModel, related_name='+')
    order = models.ForeignKey(PurchaseOrder, related_name='+')

    class Meta:
        ordering = ('-pk',)
        verbose_name_plural = _('Purchase Order Items')
        verbose_name = _('Purchase Order Item')
        unique_together = ('product', 'order')

    def __str__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('purchase_purchaseorderitem_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('purchase_purchaseorderitem_update', args=(self.slug,))
