import re
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response

from products.models import Products


from supplier.models import Supplier
from products.api.serializers import ProductsSerailizers
from .serializers import SupplierSerializers


class HomeSupplierList(generics.ListAPIView):
    queryset = Supplier.objects.all()[:9]
    serializer_class = SupplierSerializers


class SupplierDetails(generics.RetrieveAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializers
    lookup_field = 'slug'


def infinite_scroll_brands(request):
    limit = request.GET.get('limit')
    offset = request.GET.get('offset')
    cat = request.GET.get('cat')
    supplier_slug = request.GET.get('supplier')

    print(supplier_slug)

    brand_qs = get_object_or_404(Supplier, slug=supplier_slug)
    print('brands_qs', brand_qs)

    if cat == 'All Products':
        qs = Products.objects.filter(
            supplier=brand_qs
        )
        print('All Products', qs)
        return qs[int(offset): int(offset) + int(limit)]
    else:
        qs = Products.objects.filter(
            supplier=brand_qs,
            category__name__icontains=cat
        )
        print('All Products-2', qs)

        return qs[int(offset): int(offset) + int(limit)]


class SupplierProductsByCategory(generics.ListAPIView):
    serializer_class = ProductsSerailizers

    def get_queryset(self):
        qs = infinite_scroll_brands(self.request)
        return qs

    def list(self, request, *args, **kwargs):
        qs = self.get_queryset()
        print(qs)
        serializer = ProductsSerailizers(qs, many=True)
        return Response({
            "products": serializer.data
        }, status=status.HTTP_200_OK)


def infinite_scroll_category(request):
    limit = request.GET.get('limit')
    offset = request.GET.get('offset')
    cat = request.GET.get('cat')
    print(limit, offset, cat)

    if cat == 'All Brands':
        qs = Supplier.objects.all()
        print('All Products', qs)

        return qs[int(offset): int(offset) + int(limit)]
    else:
        qs = Supplier.objects.filter(
            category__name=cat
        )
        print('All Products--2', qs)

        return qs[int(offset): int(offset) + int(limit)]


class SupplierByCategory(generics.ListAPIView):
    def get_queryset(self):
        qs = infinite_scroll_category(self.request)
        return qs

    def list(self, request, *args, **kwargs):
        qs = self.get_queryset()
        print('supplier list', qs)
        serializer = SupplierSerializers(qs, many=True)
        return Response({
            "brands": serializer.data
        }, status=status.HTTP_200_OK)
