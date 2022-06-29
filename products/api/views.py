import re
from unicodedata import category
from webbrowser import get
from django.shortcuts import get_object_or_404
from rest_framework import generics, views, status, permissions
from rest_framework.response import Response

from .serializers import (
    CategoriesSerailizers,
    ProductSerializerMinimal,
    SaubCategorySerailizers,
    VariantsSerailizers,
    ProductImagesSerailizers,
    ProductsSerailizers,
)

from category.models import (
    Category,
    SubCategory,
)

from products.models import (

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


class FetchProductsByCategory1(views.APIView):
    def get(self, request, *args, **kwargs):
        category = request.query_params.get('cat')
        sub_category = request.query_params.get('sub_cat')
        category_qs = SubCategory.objects.filter(
            category__name__iexact=category
        )

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
            serialize = ProductsSerailizers(qs, many=True)
            return Response({
                "products": serialize.data,
                "category_qs": category_qs_serialize.data
            }, status=status.HTTP_200_OK)
        elif category is not None:
            qs = Products.objects.filter(
                category__name__icontains=category,
            )

            serialize = ProductsSerailizers(qs, many=True)
            return Response({
                "products": serialize.data,
                "category_qs": category_qs_serialize.data
            }, status=status.HTTP_200_OK)


class GetProductsByBrands(views.APIView):
    def get(self, request, *args, **kwargs):
        brand_name = request.query_params['brand_name']
        print('brands.............', brand_name)

        if brand_name is None:
            print('brand_name', )
            return Response({"err": "brand_name is not provide"}, status=status.HTTP_400_BAD_REQUEST)
        product_qs = Products.objects.filter(
            supplier_name=brand_name
        )

        print('brand_name', product_qs)

        serailizer = ProductsSerailizers(product_qs, many=True)
        return Response({"products": serailizer.data}, status=status.HTTP_200_OK)


class GetAllCategories(views.APIView):
    def get(self, request, *args, **kwargs):
        category_qs = Category.objects.all().order_by('-created_at')
        serializer = CategoriesSerailizers(category_qs, many=True)
        return Response({
            "categories": serializer.data
        }, status=status.HTTP_200_OK)


def is_there_more(qs, offset):
    if int(offset) > qs.count():
        return False
    return True


def infinit_scroll(request):
    limit = request.GET.get('limit')
    offset = request.GET.get('offset')
    return Products.objects.filter(is_featured=True)[int(offset): int(offset) + int(limit)]


class GetFeaturedProducts(generics.ListAPIView):
    serializer_class = ProductsSerailizers

    def get_queryset(self):
        qs = infinit_scroll(self.request)
        return qs

    def list(self, request, *args, **kwargs):
        cat_qs = Category.objects.all().order_by('-created_at')
        cat_serializers = CategoriesSerailizers(cat_qs, many=True)
        p_qs = Products.objects.filter(
            is_featured=True).order_by('-created_at')
        serializer = ProductsSerailizers(p_qs, many=True)
        qs = self.get_queryset()
        serializer = ProductsSerailizers(qs, many=True)
        return Response({
            "featured": serializer.data,
            "featured": serializer.data,
            "cat_qs": cat_serializers.data,
            "hasMore": is_there_more(qs, request.GET.get('offset'))
        })


def infinite_scroll_category(request):
    limit = request.GET.get('limit')
    offset = request.GET.get('offset')
    category = request.query_params.get('cat')
    sub_category = request.query_params.get('sub_cat')
    print('sub_category', sub_category)

    if sub_category == 'All Products':
        qs = Products.objects.filter(
            category__name__icontains=category,
        )
        print('qs', qs)
        return qs[int(offset): int(offset) + int(limit)]
    if category and sub_category is not None:
        qs = Products.objects.filter(
            category__name__icontains=category,
            sub_category__name__icontains=sub_category,
        )
        return qs[int(offset): int(offset) + int(limit)]
    elif category is not None:
        qs = Products.objects.filter(
            category__name__icontains=category,
        )
        return qs[int(offset): int(offset) + int(limit)]


class FetchProductsByCategory(generics.ListAPIView):
    serializer_class = ProductsSerailizers

    def get_queryset(self):
        qs = infinite_scroll_category(self.request)
        category = self.request.query_params.get('cat')
        category_qs = SubCategory.objects.filter(
            category__name__iexact=category
        )

        return qs, category_qs

    def list(self, request, *args, **kwargs):
        qs, category_qs = self.get_queryset()
        print(qs, category_qs)
        serialize = ProductsSerailizers(qs, many=True)
        category_qs_serialize = SaubCategorySerailizers(category_qs, many=True)

        return Response({
            "products": serialize.data,
            "category_qs": category_qs_serialize.data
        }, status=status.HTTP_200_OK)


def infinit_scroll_popular(request):
    limit = request.GET.get('limit')
    offset = request.GET.get('offset')
    return Products.objects.filter(is_featured=True)[int(offset): int(offset) + int(limit)]


class GetPopularProducts(generics.ListAPIView):
    serializer_class = ProductsSerailizers

    def get_queryset(self):
        qs = infinit_scroll_popular(self.request)
        category_qs = Category.objects.all()
        print(qs)
        return qs, category_qs

    def list(self, request, *args, **kwargs):
        cat_qs = Category.objects.all().order_by('-created_at')
        cat_serializers = CategoriesSerailizers(cat_qs, many=True)
        p_qs = Products.objects.filter(
            is_popular=True).order_by('-created_at')
        serializer = ProductsSerailizers(p_qs, many=True)
        qs = self.get_queryset()
        serializer = ProductsSerailizers(qs, many=True)
        return Response({
            "popular": serializer.data,
            "cat_qs": cat_serializers.data,
            "hasMore": is_there_more(qs, request.GET.get('offset'))
        })
