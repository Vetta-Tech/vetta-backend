from rest_framework import serializers

from cart.api.serializers import FinalCartSerializers
from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    final_cart = FinalCartSerializers(many=False, read_only=True)

    class Meta:
        model = Order
        fields = [
            'user',
            'order_id',
            'final_cart',
            'shipping_charge',
            'order_sub_total',
            'order_total',
            'address',
            'payment_method',
            'order_status',
            'orordered',
            'ordered_date',
        ]
