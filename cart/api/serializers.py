from dataclasses import field
from rest_framework import serializers

from products.api.serializers import (
    SizeSerailizers,
    ProductsSerailizers,
    VariantsSerailizers
)
from cart.models import Cart, FinalCart


class CartSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    variant = serializers.SerializerMethodField()
    user = serializers.CharField(read_only=True)

    class Meta:
        model = Cart
        fields = (
            '__all__'
        )

    def get_product(self, obj):
        return ProductsSerailizers(obj.product).data

    def get_variant(self, obj):
        return VariantsSerailizers(obj.variant).data


class FinalCartSerializers(serializers.ModelSerializer):
    cart = CartSerializer(many=True, read_only=True)

    class Meta:
        model = FinalCart
        fields = ('__all__')
