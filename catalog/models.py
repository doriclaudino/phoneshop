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
from phoneshop.models import SlugModel, SlugName


class Brand(SlugName):

    class Meta:
        verbose_name_plural = _('Brands')
        verbose_name = _('Brand')

    def get_package_name(self):
        return __package__

    def get_absolute_url(self):
        return reverse(self.get_base_url() + '_detail', args=(self.pk,))


class Model(SlugName):

    class Meta:
        verbose_name_plural = _('Models')
        verbose_name = _('Model')

    def get_package_name(self):
        return __package__


class Product(SlugName):

    # Relationship Fields
    brand = models.ForeignKey(
        Brand, related_name='+', on_delete=models.CASCADE
    )

    class Meta:
        verbose_name_plural = _('Products')
        verbose_name = _('Product')

    def get_package_name(self):
        return __package__


class ProductModel(SlugModel):

    # Fields
    slug = extension_fields.AutoSlugField(
        populate_from=['product', 'model'], blank=True)

    # Relationship Fields
    product = models.ForeignKey(Product, related_name='+')
    model = models.ForeignKey(Model, related_name='+')

    class Meta:
        verbose_name_plural = _('Product Models')
        verbose_name = _('Product Model')
        unique_together = ('product', 'model')

    def save(self, *args, **kwargs):
        name = '{0} {1}'.format(self.product, self.model)
        self.slug = slugify(name)
        models.Model.save(self, *args, **kwargs)

    def get_package_name(self):
        return __package__
