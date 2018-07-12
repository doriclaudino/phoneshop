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
from django.utils import timezone


class PaymentType(SlugName):

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
    slug = extension_fields.AutoSlugField(
        populate_from=['type', 'status', 'amount'], blank=True)
    date = models.DateTimeField(
        editable=True, default=timezone.now)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    # Relationship Fields
    type = models.ForeignKey(
        PaymentType, related_name='+')
    status = models.ForeignKey(PaymentStatus, related_name='+')

    class Meta:
        verbose_name_plural = _('Payments')
        verbose_name = _('Payment')

    def get_package_name(self):
        return __package__

    def save(self, *args, **kwargs):
        name = '{0} {1} {2}'.format(self.type, self.status, self.amount)
        self.slug = slugify(name)
        models.Model.save(self, *args, **kwargs)


class OrderPayments(SlugModel):

    # Fields
    slug = extension_fields.AutoSlugField(
        populate_from=['order', 'payment'], blank=True)

    # Relationship Fields
    order = models.ForeignKey(SellOrder, related_name='+')
    payment = models.ForeignKey(Payment, related_name='+')

    class Meta:
        verbose_name_plural = _('Order Payments')
        verbose_name = _('Order Payment')
        unique_together = ('order', 'payment')

    def get_package_name(self):
        return __package__

    def save(self, *args, **kwargs):
        name = '{0} {1}'.format(self.order, self.payment)
        self.slug = slugify(name)
        models.Model.save(self, *args, **kwargs)
