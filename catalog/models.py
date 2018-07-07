from django.core.urlresolvers import reverse
from django_extensions.db.fields import AutoSlugField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields
from django.utils.translation import gettext_lazy as _


class Brand(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    objects = models.Manager()

    class Meta:
        ordering = ('-pk',)
        verbose_name_plural = _('Brands')
        verbose_name = _('Brand')

    def __str__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('catalog_brand_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('catalog_brand_update', args=(self.slug,))


# Represent the models of products
class Model(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    objects = models.Manager()

    class Meta:
        ordering = ('-pk',)
        verbose_name_plural = _('Models')
        verbose_name = _('Model')

    def __str__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('catalog_model_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('catalog_model_update', args=(self.slug,))


class Product(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    objects = models.Manager()

    # Relationship Fields
    brand = models.ForeignKey(
        Brand, related_name='+', on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('-pk',)
        verbose_name_plural = _('Products')
        verbose_name = _('Product')

    def __str__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('catalog_product_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('catalog_product_update', args=(self.slug,))


class ProductModel(models.Model):

    # Fields
    slug = extension_fields.AutoSlugField(
        populate_from=['product', 'model'], blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    objects = models.Manager()

    # Relationship Fields
    product = models.ForeignKey(Product, related_name='+')
    model = models.ForeignKey(Model, related_name='+')

    class Meta:
        ordering = ('-pk',)
        verbose_name_plural = _('Product Models')
        verbose_name = _('Product Model')

    def __str__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('catalog_productmodel_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('catalog_productmodel_update', args=(self.slug,))
