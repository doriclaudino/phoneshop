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


class Location(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    objects = models.Manager()

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = _('Locations')
        verbose_name = _('Location')

    def __str__(self):
        return '%s' % self.slug

    def get_absolute_url(self):
        return reverse('logistic_location_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('logistic_location_update', args=(self.slug,))


class Carrier(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    website = models.CharField(max_length=100, blank=True)
    tracking_url = models.CharField(max_length=100, blank=True)
    slug = AutoSlugField(populate_from='name', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    objects = models.Manager()

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = _('Carriers')
        verbose_name = _('Carrier')

    def __str__(self):
        return '%s' % self.slug

    def get_absolute_url(self):
        return reverse('logistic_carrier_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('logistic_carrier_update', args=(self.slug,))


class TrackingStatus(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    objects = models.Manager()

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = _('Tracking Statuses')
        verbose_name = _('Tracking Status')

    def __str__(self):
        return '%s' % self.slug

    def get_absolute_url(self):
        return reverse('logistic_trackingstatus_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('logistic_trackingstatus_update', args=(self.slug,))


class Tracking(models.Model):

    # Fields
    number = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from=['number', 'carrier'], blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    description = models.TextField(max_length=100,  blank=True)
    objects = models.Manager()

    # Relationship Fields
    status = models.ForeignKey(TrackingStatus, related_name='+')
    previous = models.ForeignKey(
        'self', related_name='+', blank=True, null=True)
    carrier = models.ForeignKey(Carrier, related_name='+')

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = _('Trackings')
        verbose_name = _('Tracking')

    def __str__(self):
        return '%s' % self.slug

    def get_absolute_url(self):
        return reverse('logistic_tracking_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('logistic_tracking_update', args=(self.slug,))
