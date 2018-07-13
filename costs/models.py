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
from payments.models import Payment
from sales.models import SellOrder
from inventory.models import Item
from purchase.models import PurchaseOrder
from sales.models import SellOrder
from phoneshop.models import SlugName, SlugModel
from logistic.models import Tracking


class CostType(SlugName):

    class Meta:
        verbose_name_plural = _('Cost Types')
        verbose_name = _('Cost Type')

    def get_package_name(self):
        return __package__


class Cost(SlugModel):

    # Fields
    slug = extension_fields.AutoSlugField(
        populate_from=['type', 'payment'], blank=True)
    details = models.TextField(max_length=400, blank=True)

    # Relationship Fields
    type = models.ForeignKey(CostType, related_name='+')
    payment = models.ForeignKey(Payment, related_name='+', blank=True)

    class Meta:
        verbose_name_plural = _('Costs')
        verbose_name = _('Cost')

    def get_package_name(self):
        return __package__

    def save(self, *args, **kwargs):
        name = '{0} {1}'.format(self.type, self.payment)
        self.slug = slugify(name)
        models.Model.save(self, *args, **kwargs)


class Costs(SlugModel):
    # Fields
    slug = extension_fields.AutoSlugField(
        populate_from=['ref', 'cost'], blank=True)

    # Relationship Fields
    ref = ''
    cost = models.ForeignKey(Cost, related_name='+', blank=True)

    class Meta:
        verbose_name_plural = _('Costs')
        verbose_name = _('Cost')

    def get_package_name(self):
        return __package__

    def save(self, *args, **kwargs):
        name = '{0} {1}'.format(self.ref, self.cost)
        self.slug = slugify(name)
        models.Model.save(self, *args, **kwargs)


class PurchaseCosts(Costs):
    ref = models.ForeignKey(PurchaseOrder, related_name='+')

    class Meta:
        verbose_name_plural = _('Purchase Costs')
        verbose_name = _('Purchase Cost')


class SellCosts(Costs):
    ref = models.ForeignKey(SellOrder, related_name='+')

    class Meta:
        verbose_name_plural = _('Sell Costs')
        verbose_name = _('Sell Cost')


class ItemCosts(Costs):
    ref = models.ForeignKey(Item, related_name='+')

    class Meta:
        verbose_name_plural = _('Item Costs')
        verbose_name = _('Item Cost')


class TrackingCosts(Costs):
    ref = models.ForeignKey(Tracking, related_name='+')

    class Meta:
        verbose_name_plural = _('Tracking Costs')
        verbose_name = _('Tracking Cost')
