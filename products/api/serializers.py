from dataclasses import fields
from pyexpat import model
from rest_framework import serializers

from taggit.serializers import (
    TagListSerializerField,
    TaggitSerializer
)

from category.api.serializers import (
    CategoriesSerailizers,
    SaubCategorySerailizers
)

from products.models import (
    Products,
    ProductImages,
    Color,
    Size,
    Variants,
    Supplier
)


class ProductImagesSerailizers(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = (
            '__all__'
        )


class ColorSerailizers(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = (
            '__all__'
        )


class SizeSerailizers(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = (
            '__all__'
        )


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = (
            '__all__'
        )


class VariantsSerailizers(serializers.ModelSerializer):
    size = SizeSerailizers(many=False)

    class Meta:
        model = Variants
        fields = (
            'id',
            'title',
            'product',
            'size',
            'quantity',
            'price',
        )


class ProductSerializerMinimal(serializers.ModelSerializer, TaggitSerializer):
    class Meta:
        model = Products
        fields = (
            'supplier_name',
            'name',
            'slug',
            'category',
            'thumbnail',
            'price',
            'status',
            'is_featured'
        )


class ProductsSerailizers(serializers.ModelSerializer, TaggitSerializer):
    category = CategoriesSerailizers(many=False)
    sub_category = SaubCategorySerailizers(many=False)
    variants = VariantsSerailizers(many=True, read_only=True)
    keywords = TagListSerializerField()
    supplier = SupplierSerializer()
    images = ProductImagesSerailizers(many=True, read_only=True)

    class Meta:
        model = Products
        fields = (
            'id',
            'supplier_name',
            'name',
            'supplier',
            'slug',
            'category',
            'sub_category',
            'short_description',
            'description',
            'keywords',
            'images',
            'variants',
            'thumbnail',
            'price',
            'variant',
            'status',
            'created_at',
            'updated_at',
        )
