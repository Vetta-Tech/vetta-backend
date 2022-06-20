from django.utils import timezone
from django.shortcuts import get_object_or_404
from rest_framework import views, generics, status
from rest_framework.response import Response
from .serializers import CartSerializer

from products.models import Products, Variants
from cart.models import Cart, FinalCart


class AddToCart(views.APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        # print(user)
        if user.is_authenticated:
            slug = request.data.get('slug', None)
            variant_id = request.data.get('variant_id', None)

            if slug is None:
                return Response({
                    "msg"  "Something went wrong"
                }, status=status.HTTP_400_BAD_REQUEST)

            item = get_object_or_404(Products, slug=slug)

            if variant_id is not None:
                variant_qs = get_object_or_404(Variants, id=variant_id)
                print(variant_qs)
                if variant_qs:
                    order_item = Cart.objects.create(
                        user=user,
                        product=item,
                        variant=variant_qs,
                        expires=False
                    )
                    total_price = variant_qs.price
                    print(variant_qs.price)
            else:
                order_item = Cart.objects.create(
                    user=user,
                    product=item,
                    expires=False
                )
                total_price = item.price
                print(item.price)
                order_item.save()
            cart_serializer = CartSerializer(order_item)

            order_qs = FinalCart.objects.filter(
                user=user, expires=False
            )

            if order_qs.exists():
                order = order_qs[0]
                if not order.cart.filter(product__id=order_item.id).exists():
                    order.cart.add(order_item)
                    order.sub_total += total_price
                    order.save()
                    return Response({
                        "item": cart_serializer.data,
                        "success": "OK"
                    }, status=status.HTTP_200_OK)
                else:
                    return Response({
                        "msg": "Something went wrong"
                    }, status=status.HTTP_200_OK)
            else:
                ordered_data = timezone.now()
                order = FinalCart.objects.create(
                    ordered_date=ordered_data,
                    user=user,
                    sub_total=total_price,
                    expires=False
                )
                order.cart.add(order_item)
                return Response({
                    "item": cart_serializer.data,
                    "success": "OK"
                }, status=status.HTTP_200_OK)
        else:
            return Response({
                'msg': 'Not Authorized'
            }, status=status.HTTP_401_UNAUTHORIZED)


class CheckCanAddToCart(views.APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            variant_id = request.data.get('variant_id', None)
            product = request.data.get('product', None)
            print(product, variant_id)
            procust_qs = get_object_or_404(Products, slug=product)
            variants_qs = Variants.objects.filter(
                id=variant_id
            )
            if variants_qs:
                variants = variants_qs[0]
                cart_qs = Cart.objects.filter(
                    user=user,
                    variant=variants,
                    expires=False
                )
                if cart_qs:
                    print('cart_qs', cart_qs)
                    return Response({
                        "msg": "False"
                    }, status=status.HTTP_200_OK)
                else:
                    return Response({
                        "msg": "True"
                    }, status=status.HTTP_200_OK)
            else:
                cart_qs = Cart.objects.filter(
                    user=user,
                    product=procust_qs,
                    expires=False
                )
                if cart_qs:
                    return Response({
                        "msg": "False"
                    }, status=status.HTTP_200_OK)
                else:
                    return Response({
                        "msg": "True"
                    }, status=status.HTTP_200_OK)
        else:
            return Response({
                "msg": "Unauthorized request"
            }, status=status.HTTP_400_BAD_REQUEST)
