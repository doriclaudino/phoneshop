from django.core.urlresolvers import reverse
from django_extensions.db.fields import AutoSlugField, slugify
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields
from django.utils.translation import gettext_lazy as _
from logistic.models import Tracking
from inventory.models import Item
from phoneshop.models import SlugModel, SlugName


class Seller(SlugName):

    website = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = _('Sellers')
        verbose_name = _('Seller')

    def get_package_name(self):
        return __package__


class SellOrderStatus(SlugName):

    class Meta:
        verbose_name = _('Order Status')
        verbose_name_plural = _('Order Statuses')

    def get_package_name(self):
        return __package__


class SellOrder(SlugModel):
    # Fields
    details = models.TextField(max_length=500, blank=True)
    slug = extension_fields.AutoSlugField(
        populate_from=['seller', 'tracking'], blank=True)

    # Relationship Fields
    seller = models.ForeignKey(Seller, related_name='+')
    status = models.ForeignKey(SellOrderStatus, related_name='+')
    tracking = models.ForeignKey(Tracking, related_name='+', blank=True)

    class Meta:
        verbose_name_plural = _('Sell Orders')
        verbose_name = _('Sell Order')
        unique_together = ('seller', 'tracking')

    def save(self, *args, **kwargs):
        name = '{0} {1}'.format(self.seller, self.tracking)
        self.slug = slugify(name)
        super(SellOrder, self).save(*args, **kwargs)

    def get_package_name(self):
        return __package__


class SellOrderItem(SlugModel):

    # Fields
    slug = extension_fields.AutoSlugField(
        populate_from=['order', 'product', 'quantity', 'price'], blank=True)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, default=100.00)

    # Relationship Fields
    product = models.ForeignKey(Item, related_name='+')
    order = models.ForeignKey(SellOrder, related_name='+')

    class Meta:
        verbose_name_plural = _('Sell Order Items')
        verbose_name = _('Sell Order Item')
        unique_together = ('product', 'order')

    def save(self, *args, **kwargs):
        name = '{0} {1} {2} {3}'.format(
            self.order, self.product, self.quantity, self.price)
        self.slug = slugify(name)
        super(SellOrderItem, self).save(*args, **kwargs)

    def get_package_name(self):
        return __package__
