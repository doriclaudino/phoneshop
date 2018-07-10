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
from catalog.models import ProductModel
from phoneshop.models import SlugModel, SlugName, SlugOrderItem


class Supplier(SlugName):

    website = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = _('Suppliers')
        verbose_name = _('Supplier')

    def get_package_name(self):
        return __package__


class PurchaseOrderStatus(SlugName):

    class Meta:
        verbose_name_plural = _('Purchase Order Statuses')
        verbose_name = _('Purchase Order Status')

    def get_package_name(self):
        return __package__


class PurchaseOrder(SlugModel):

    # Fields
    details = models.TextField(max_length=500, blank=True)
    slug = extension_fields.AutoSlugField(
        populate_from=['supplier', 'tracking'], blank=True)

    # Relationship Fields
    supplier = models.ForeignKey(Supplier, related_name='+')
    status = models.ForeignKey(PurchaseOrderStatus, related_name='+')
    tracking = models.ForeignKey(Tracking, related_name='+', blank=True)

    class Meta:
        verbose_name_plural = _('Purchase Orders')
        verbose_name = _('Purchase Order')
        unique_together = ('supplier', 'tracking')

    def get_package_name(self):
        return __package__

    def save(self, *args, **kwargs):
        name = '{0} {1}'.format(self.supplier, self.tracking)
        self.slug = slugify(name)
        models.Model.save(self, *args, **kwargs)


class PurchaseOrderItem(SlugOrderItem):

    # Relationship Fields
    product = models.ForeignKey(ProductModel, related_name='+')
    order = models.ForeignKey(PurchaseOrder, related_name='+')

    def get_package_name(self):
        return __package__
