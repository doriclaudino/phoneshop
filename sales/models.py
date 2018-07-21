from django.core.urlresolvers import reverse
from django_extensions.db.fields import AutoSlugField, slugify
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.db import models as models
from django_extensions.db import fields as extension_fields
from django.utils.translation import gettext_lazy as _
from logistic.models import Tracking
from inventory.models import Item
from phoneshop.models import SlugModel, SlugName, SlugOrderItem


class Customer(SlugName):

    user = models.ForeignKey(
        get_user_model(), related_name='+', null=True, blank=True)

    class Meta:
        verbose_name_plural = _('Customers')
        verbose_name = _('Customer')
        unique_together = ['name', 'user']

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
        populate_from=['seller', 'status', 'tracking'], blank=True)

    # Relationship Fields
    seller = models.ForeignKey(get_user_model(), related_name='+')
    customer = models.ForeignKey(
        Customer, related_name='+', null=True, blank=True)
    status = models.ForeignKey(SellOrderStatus, related_name='+')
    tracking = models.ForeignKey(Tracking, related_name='+', blank=True)

    class Meta:
        verbose_name_plural = _('Sell Orders')
        verbose_name = _('Sell Order')
        unique_together = ('seller', 'tracking')

    def save(self, *args, **kwargs):
        name = '{0} {1} {2}'.format(self.seller, self.status, self.tracking)
        self.slug = slugify(name)
        models.Model.save(self, *args, **kwargs)

    def get_package_name(self):
        return __package__


class SellOrderItem(SlugOrderItem):

    # Relationship Fields
    product = models.ForeignKey(Item, related_name='+')
    order = models.ForeignKey(SellOrder, related_name='+')

    def get_package_name(self):
        return __package__
