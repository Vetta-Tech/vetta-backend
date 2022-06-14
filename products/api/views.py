from nis import cat
import re
from webbrowser import get
from django.shortcuts import get_object_or_404
from rest_framework import generics, views, status, permissions
from rest_framework.response import Response

from .serializers import (
    ProductSerializerMinimal,
    SaubCategorySerailizers,
    VariantsSerailizers,
    ProductImagesSerailizers,
    ProductsSerailizers,
)

from products.models import (
    Category,
    Products,
    SubCategory,
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
        print(slug)
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


class HomeProductsApiView(views.APIView):
    def get(self, request, *args, **kwargs):
        featured = Products.objects.filter(
            is_featured=True
        ).order_by('-created_at')
        recent_products = Products.objects.all().order_by('created_at')[:15]
        popular = Products.objects.filter(
            is_popular=True
        ).order_by('-created_at')
        electronics = SubCategory.objects.filter(
            category__name='Electronics'
        )
        footwear = SubCategory.objects.filter(
            category__name='Footwear'
        )
        baby_care = SubCategory.objects.filter(
            category__name='Baby Care'
        )

        f_qs = ProductsSerailizers(featured, many=True)
        r_qs = ProductsSerailizers(recent_products, many=True)
        p_qs = ProductsSerailizers(popular, many=True)

        electronics_qs = SaubCategorySerailizers(electronics, many=True)
        footwear_qs = SaubCategorySerailizers(footwear, many=True)
        baby_care_qs = SaubCategorySerailizers(baby_care, many=True)

        return Response({
            "featured": f_qs.data,
            "recent_products": r_qs.data,
            "popular": p_qs.data,
            "electronics": electronics_qs.data,
            "footwear": footwear_qs.data,
            "baby_care": baby_care_qs.data
        }, status=status.HTTP_200_OK)


class FetchProductsByCategory(views.APIView):
    def get(self, request, *args, **kwargs):
        category = request.query_params.get('cat')
        sub_category = request.query_params.get('sub_cat')
        category_qs = SubCategory.objects.filter(
            category__name__iexact=category
        )

        print('asdasd', category)

        print(category)

        category_qs_serialize = SaubCategorySerailizers(category_qs, many=True)
        if sub_category == 'All Products':
            qs = Products.objects.filter(
                category__name__icontains=category,
            )
            serialize = ProductsSerailizers(qs, many=True)
            return Response({
                "products": serialize.data,
                "category_qs": category_qs_serialize.data
            }, status=status.HTTP_200_OK)

        if category and sub_category is not None:
            qs = Products.objects.filter(
                category__name__icontains=category,
                sub_category__name__icontains=sub_category,
            )
            print('qs both', qs)
            serialize = ProductsSerailizers(qs, many=True)
            return Response({
                "products": serialize.data,
                "category_qs": category_qs_serialize.data
            }, status=status.HTTP_200_OK)
        elif category is not None:
            qs = Products.objects.filter(
                category__name__icontains=category,
            )
            print('qs one', qs)

            serialize = ProductsSerailizers(qs, many=True)
            return Response({
                "products": serialize.data,
                "category_qs": category_qs_serialize.data
            }, status=status.HTTP_200_OK)
