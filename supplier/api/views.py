from rest_framework import generics

from supplier.models import Supplier
from .serializers import SupplierSerializers


class HomeSupplierList(generics.ListAPIView):
    queryset = Supplier.objects.all()[:9]
    serializer_class = SupplierSerializers
