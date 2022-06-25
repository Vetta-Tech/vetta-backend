from rest_framework import serializers
from rest_framework.response import Response

from address.models import Address


class AddressSerializers(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)

    class Meta:
        model = Address
        fields = (
            '__all__'
        )
