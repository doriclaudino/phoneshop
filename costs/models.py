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
        populate_from=['cost_of'], blank=True)
    details = models.CharField(max_length=100, blank=True)
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, default=100.00)

    # Relationship Fields
    type = models.ForeignKey(CostType, related_name='+')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def get_package_name(self):
        return __package__

    def cost_of(self):
        return '{0} - {1}'.format(self.content_type.model, self.content_object)
