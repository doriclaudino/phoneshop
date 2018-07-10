from django.core.urlresolvers import reverse
from django_extensions.db.fields import AutoSlugField, slugify
from django.db import models as models
from django.utils.translation import gettext_lazy as _


class SlugModel(models.Model):
    # Fields
    slug = AutoSlugField(populate_from='created_at', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    objects = models.Manager()

    class Meta:
        abstract = True
        ordering = ('-pk',)

    def __str__(self):
        return '%s' % self.slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.default_slug())
        super(SlugModel, self).save(*args, **kwargs)

    def default_slug(self, *args, **kwargs):
        name = '{0} {1} {2}'.format(
            self.get_package_name(), self.get_class_name(), self.pk)
        return name

    def get_package_name(self):
        raise NotImplementedError(
            '\n def get_package_name(): \n \t return __package__')

    def get_class_name(self):
        return self.__class__.__name__

    def get_base_url(self):
        return '{0}_{1}'.format(self.get_package_name(), self.get_class_name()).lower()

    def get_absolute_url(self):
        return reverse(self.get_base_url() + '_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse(self.get_base_url() + '_update', args=(self.slug,))


class SlugName(SlugModel):
    # Fields
    slug = AutoSlugField(populate_from='name', blank=True, unique=True)
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        models.Model.save(self, *args, **kwargs)
