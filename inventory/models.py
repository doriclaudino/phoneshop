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
from catalog.models import ProductModel
from purchase.models import PurchaseOrderItem
from phoneshop.models import SlugModel, SlugName


class IdentifierType(SlugName):

    class Meta:
        verbose_name_plural = _('Identifier Types')
        verbose_name = _('Identifier Type')

    def get_package_name(self):
        return __package__


class LocalType(SlugName):

    class Meta:
        verbose_name_plural = _('Local Types')
        verbose_name = _('Local Type')

    def get_package_name(self):
        return __package__


class Local(SlugName):

    # Relationship Fields
    type = models.ForeignKey(LocalType, related_name='+')

    class Meta:
        verbose_name_plural = _('Locals')
        verbose_name = _('Local')

    def get_package_name(self):
        return __package__


class Identifier(SlugModel):

    # Fields
    value = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(
        populate_from=['type', 'value'], blank=True)

    # Relationship Fields
    type = models.ForeignKey(IdentifierType, related_name='+')

    class Meta:
        verbose_name_plural = _('Identifiers')
        verbose_name = _('Identifier')
        unique_together = ('type', 'value')

    def get_package_name(self):
        return __package__

    def save(self, *args, **kwargs):
        name = '{0} {1}'.format(self.type, self.value)
        self.slug = slugify(name)
        models.Model.save(self, *args, **kwargs)


class Item(SlugModel):

    # Fields
    slug = extension_fields.AutoSlugField(
        populate_from=['product', 'identifier'], blank=True)

    # Relationship Fields
    product = models.ForeignKey(PurchaseOrderItem, related_name='+')
    identifier = models.ForeignKey(Identifier, related_name='+')
    local = models.ForeignKey(Local, related_name='+')

    class Meta:
        verbose_name_plural = _('Items')
        verbose_name = _('Item')
        unique_together = ('product', 'identifier')

    def get_package_name(self):
        return __package__

    def save(self, *args, **kwargs):
        name = '{0} {1}'.format(self.product, self.identifier)
        self.slug = slugify(name)
        models.Model.save(self, *args, **kwargs)
