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


class Supplier(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    website = models.TextField(max_length=100)
    objects = models.Manager()

    class Meta:
        ordering = ('-pk',)
        verbose_name_plural = _('Suppliers')
        verbose_name = _('Supplier')

    def __str__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('purchase_supplier_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('purchase_supplier_update', args=(self.slug,))
