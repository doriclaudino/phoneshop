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
from costs.models import Cost


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
    slug = AutoSlugField(populate_from=['method', 'status'], blank=True)
    date = models.DateTimeField(default=timezone.now)
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, default=100.00)

    # Relationship Fields
    status = models.ForeignKey(PaymentStatus, related_name='+')
    method = models.ForeignKey(PaymentMethod, related_name='+')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name_plural = _('Payments')
        verbose_name = _('Payment')

    def get_package_name(self):
        return __package__

    def payment_of(self):
        return '{0} - {1}'.format(self.content_type.model, self.content_object)
