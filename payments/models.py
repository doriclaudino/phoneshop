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
from phoneshop.models import SlugName, SlugModel
from sales.models import SellOrder
from purchase.models import PurchaseOrder
from logistic.models import Tracking
from costs.models import Cost
from django.utils import timezone
from costs.models import TrackingCost, ItemCost, SellCost, PurchaseCost


class PaymentMethod(SlugName):

    class Meta:
        verbose_name_plural = _('Payment types')
        verbose_name = _('Payment type')

    def get_package_name(self):
        return __package__


class PaymentStatus(SlugName):

    class Meta:
        verbose_name_plural = _('Payment statuses')
        verbose_name = _('Payment status')

    def get_package_name(self):
        return __package__


class Payment(SlugModel):

    # Fields
    slug = AutoSlugField(populate_from=['ref', 'method', 'status'], blank=True)
    date = models.DateTimeField(default=timezone.now)
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, default=100.00)

    # Relationship Fields
    status = models.ForeignKey(PaymentStatus, related_name='+')
    method = models.ForeignKey(PaymentMethod, related_name='+')
    ref = ''

    class Meta:
        verbose_name_plural = _('Payments')
        verbose_name = _('Payment')
        abstract = True

    def get_package_name(self):
        return __package__

    def save(self, *args, **kwargs):
        name = '{0} {1} {2}'.format(self.ref, self.method, self.status)
        self.slug = slugify(name)
        models.Model.save(self, *args, **kwargs)


class SalePayment(Payment):
    ref = models.ForeignKey(SellOrder, related_name='+')

    class Meta:
        verbose_name_plural = _('Sale Payments')
        verbose_name = _('Sale Payment')


class PurchasePayment(Payment):
    ref = models.ForeignKey(PurchaseOrder, related_name='+')

    class Meta:
        verbose_name_plural = _('Purchase Payments')
        verbose_name = _('Purchase Payment')


class TrackingPayment(Payment):
    ref = models.ForeignKey(Tracking, related_name='+')

    class Meta:
        verbose_name_plural = _('Tracking Payments')
        verbose_name = _('Tracking Payment')


# relative costs payments
class PurchaseCostPayment(Payment):
    ref = models.ForeignKey(PurchaseCost, related_name='+')

    class Meta:
        verbose_name_plural = _('Purchase Cost Payments')
        verbose_name = _('Purchase Cost Payment')


class SellCostPayment(Payment):
    ref = models.ForeignKey(SellCost, related_name='+')

    class Meta:
        verbose_name_plural = _('Sell Cost Payments')
        verbose_name = _('Sell Cost Payment')
        #unique_together = ['','']


class ItemCostPayment(Payment):
    ref = models.ForeignKey(ItemCost, related_name='+')

    class Meta:
        verbose_name_plural = _('Item Cost Payments')
        verbose_name = _('Item Cost Payment')


class TrackingCostPayment(Payment):
    ref = models.ForeignKey(TrackingCost, related_name='+')

    class Meta:
        verbose_name_plural = _('Tracking Cost Payments')
        verbose_name = _('Tracking Cost Payment')
