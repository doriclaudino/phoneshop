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


class Carrier(SlugName):

    # Fields
    website = models.CharField(max_length=100, blank=True)
    tracking_url = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name_plural = _('Carriers')
        verbose_name = _('Carrier')

    def get_package_name(self):
        return __package__


class TrackingStatus(SlugName):

    class Meta:
        verbose_name_plural = _('Tracking Statuses')
        verbose_name = _('Tracking Status')

    def get_package_name(self):
        return __package__


class Tracking(SlugModel):

    # Fields
    number = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from=['carrier', 'number'], blank=True)
    description = models.TextField(max_length=100,  blank=True)

    # Relationship Fields
    status = models.ForeignKey(TrackingStatus, related_name='+')
    previous = models.ForeignKey(
        'self', related_name='+', blank=True, null=True)
    carrier = models.ForeignKey(Carrier, related_name='+')

    class Meta:
        verbose_name_plural = _('Trackings')
        verbose_name = _('Tracking')
        unique_together = ('carrier', 'number')

    def get_package_name(self):
        return __package__

    def save(self, *args, **kwargs):
        name = '{0} {1}'.format(self.carrier, self.number)
        self.slug = slugify(name)
        models.Model.save(self, *args, **kwargs)
