from rest_auth.models import TokenModel
from rest_framework import serializers


class RestAuthCustomSerializers(serializers.ModelSerializer):
    token = serializers.CharField(source='key')

    class Meta:
        model = TokenModel
        fields = ('token',)
