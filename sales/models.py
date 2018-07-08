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


class Seller(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    website = models.CharField(max_length=100)
    objects = models.Manager()

    class Meta:
        ordering = ('-pk',)
        verbose_name_plural = _('Sellers')
        verbose_name = _('Seller')

    def __str__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('sales_seller_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('sales_seller_update', args=(self.slug,))


class SellOrderStatus(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    objects = models.Manager()

    class Meta:
        ordering = ('-pk',)
        verbose_name_plural = _('Sell Order Statuses')
        verbose_name = _('Sell Order Status')

    def __str__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('sales_sellorderstatus_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('sales_sellorderstatus_update', args=(self.slug,))


class SellOrder(models.Model):

    # Fields
    details = models.TextField(max_length=500, blank=True)
    slug = extension_fields.AutoSlugField(
        populate_from=['seller', 'tracking'], blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    objects = models.Manager()

    # Relationship Fields
    seller = models.ForeignKey(Seller, related_name='+')
    status = models.ForeignKey(SellOrderStatus, related_name='+')
    tracking = models.ForeignKey(Tracking, related_name='+', blank=True)

    class Meta:
        ordering = ('-pk',)
        verbose_name_plural = _('Sell Orders')
        verbose_name = _('Sell Order')

    def __str__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('sales_sellorder_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('sales_sellorder_update', args=(self.slug,))


class SellOrderItem(models.Model):

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
    order = models.ForeignKey(SellOrder, related_name='+')

    class Meta:
        ordering = ('-pk',)
        verbose_name_plural = _('Sell Order Items')
        verbose_name = _('Sell Order Item')

    def __str__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('sales_sellorderitem_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('sales_sellorderitem_update', args=(self.slug,))
