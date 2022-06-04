from django.shortcuts import get_object_or_404
from rest_framework import generics, views, status
from rest_framework.response import Response

from .serializers import (
    VariantsSerailizers,
    ProductImagesSerailizers,
    ProductsSerailizers,
)

from products.models import (
    Category,
    Products,
    ProductImages,
    Color,
    Size,
    Variants,
)


class ProductListApiView(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerailizers


class ProductDetailsApiView(views.APIView):
    def get(self, request, *args, **kwargs):
        slug = self.kwargs['slug']
        product = get_object_or_404(Products, slug=slug)
        images_qs = ProductImages.objects.filter(
            product=product
        )
        variants_qs = Variants.objects.filter(
            product=product
        )
        products_serializer = ProductsSerailizers(product)
        products_image_serializer = ProductImagesSerailizers(
            images_qs, many=True)
        variants_serilizer = VariantsSerailizers(variants_qs, many=True)
        return Response({
            'products': products_serializer.data,
            'images': products_image_serializer.data,
            'variants': variants_serilizer.data
        }, status=status.HTTP_200_OK)
