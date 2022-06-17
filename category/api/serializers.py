from rest_framework import serializers

from taggit.serializers import (
    TagListSerializerField,
    TaggitSerializer
)

from category.models import (
    Category,
    SubCategory
)


class CategoriesSerailizers(serializers.ModelSerializer, TaggitSerializer):
    keywords = TagListSerializerField()

    class Meta:
        model = Category
        fields = (
            '__all__'
        )


class SaubCategorySerailizers(serializers.ModelSerializer, TaggitSerializer):
    keywords = TagListSerializerField()
    category = CategoriesSerailizers(many=False)

    class Meta:
        model = SubCategory
        fields = (
            'id',
            'name',
            'slug',
            'keywords',
            'description',
            'category',
            'image',
            'status',
            'created_at',
            'updated_at',
        )
