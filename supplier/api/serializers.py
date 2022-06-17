from rest_framework import serializers

from category.api.serializers import (
    CategoriesSerailizers
)
from supplier.models import Supplier


class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return


class SupplierSerializers(serializers.ModelSerializer):

    category = CategoriesSerailizers(many=True, read_only=True)

    class Meta:
        model = Supplier
        depth = 1
        fields = [
            'name',
            'slug',
            'descrition',
            'logo',
            'cover_image',
            'category',
            'active',
            'created_at',
        ]
