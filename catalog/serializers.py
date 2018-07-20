from . import models

from rest_framework import serializers


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Brand
        fields = (
            'pk',
            'slug',
            'name',
            'created_at',
            'updated_at',
        )
