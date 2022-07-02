from itertools import product
from django.utils import timezone
from django.shortcuts import get_object_or_404
from rest_framework import views, generics, status
from rest_framework.response import Response
from .serializers import CartSerializer, FinalCartSerializers

from products.models import Products, Variants
from cart.models import Cart, FinalCart
from coupon.models import Coupon


class UserCartListApiView(views.APIView):
    def get(self, request, *args, **kwargs):
        user = self.request.user
        if user.is_authenticated:
            final_qs = FinalCart.objects.filter(
                user=user, expires=False).first()
            if final_qs:
                cart_qs = final_qs.cart.filter(quantity__gt=0)
                serailizer = CartSerializer(cart_qs, many=True)
                final_qs_serializer = FinalCartSerializers(final_qs)

                return Response({
                    "cart_qs": serailizer.data,
                    "final_cart": final_qs_serializer.data,
                    "lenght": len(final_qs.cart.all())
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "msg": "No cart",
                    "lenght": 0
                }, status=status.HTTP_200_OK)
        else:
            return Response({
                "msg": "No cart"
            }, status=status.HTTP_400_BAD_REQUEST)


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
                if variant_qs:
                    order_item = Cart.objects.create(
                        user=user,
                        product=item,
                        variant=variant_qs,
                        expires=False,
                        quantity=1
                    )
                    total_price = variant_qs.price
            else:
                order_item = Cart.objects.create(
                    user=user,
                    product=item,
                    expires=False,
                    quantity=1
                )
                total_price = item.price
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
                    order.total += total_price
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
                    total=total_price,
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
            print('procust_qs', procust_qs)
            variants_qs = Variants.objects.filter(
                id=variant_id
            )
            if variants_qs:
                variants = variants_qs[0]
                cart_qs = Cart.objects.filter(
                    user=user,
                    variant=variants,
                    expires=False
                ).first()
                if cart_qs:
                    print(cart_qs.quantity)
                    seralizer = CartSerializer(cart_qs)
                    return Response({
                        "msg": "False",
                        "cart_qs": seralizer.data
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
                ).first()
                seralizer = CartSerializer(cart_qs)
                if cart_qs:
                    return Response({
                        "msg": "False",
                        "cart_qs": seralizer.data
                    }, status=status.HTTP_200_OK)
                else:
                    return Response({
                        "msg": "True"
                    }, status=status.HTTP_200_OK)
        else:
            return Response({
                "msg": "Unauthorized request"
            }, status=status.HTTP_400_BAD_REQUEST)


class PlusQuantity(views.APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        cart_id = request.data.get('id', None)
        variant_id = request.data.get('variant_id', None)
        print(cart_id, variant_id)
        if user.is_authenticated and cart_id is not None:
            cart_qs = get_object_or_404(Cart, id=cart_id)
            cart_qs.quantity += 1
            cart_qs.save()
            if variant_id is not None:
                qs = get_object_or_404(Variants, id=variant_id)
                total_price = qs.price
            else:
                total_price = cart_qs.product.price
            final_cart_qs = FinalCart.objects.filter(
                user=user, expires=False
            ).first()
            print('total_price', total_price)
            final_cart_qs.sub_total += total_price
            final_cart_qs.total += total_price
            final_cart_qs.save()
            return Response({
                "msg": "Cart Quantity Updated"
            }, status=status.HTTP_200_OK)
        return Response({
            "msg": "somethng went wrong"
        }, status=status.HTTP_400_BAD_REQUEST)


class MinusQuantity(views.APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        cart_id = request.data.get('id', None)
        variant_id = request.data.get('variant_id', None)

        if user.is_authenticated and cart_id is not None:
            cart_qs = get_object_or_404(Cart, id=cart_id)
            cart_qs.quantity -= 1
            cart_qs.save()
            if variant_id is not None:
                qs = get_object_or_404(Variants, id=variant_id)
                total_price = qs.price
            else:
                total_price = cart_qs.product.price
            final_cart_qs = FinalCart.objects.filter(
                user=user, expires=False
            ).first()
            print('total_price', total_price)
            final_cart_qs.sub_total -= total_price
            final_cart_qs.total -= total_price
            final_cart_qs.save()
            if cart_qs.quantity == 0:
                cart_qs.delete()
                if len(final_cart_qs.cart.all()) <= 0:
                    final_cart_qs.delete()
            return Response({
                "msg": "Cart Quantity Updated"
            }, status=status.HTTP_200_OK)
        return Response({
            "msg": "somethng went wrong"
        }, status=status.HTTP_400_BAD_REQUEST)


class CouponAddedApi(views.APIView):
    def post(self, request, *args, **kwargs):
        coupon_code = request.data.get('coupon_code', None)
        print('coupon qs', coupon_code)

        final_cart_id = request.data.get('final_cart_id', None)
        if coupon_code and final_cart_id is not None:
            coupon_qs = get_object_or_404(Coupon, code=coupon_code)
            final_cart_qs = get_object_or_404(FinalCart, id=final_cart_id)

            if final_cart_qs.coupon is None:
                if coupon_qs and final_cart_qs:
                    final_cart_qs.total = final_cart_qs.total - coupon_qs.discount_amount
                    final_cart_qs.total_saved = coupon_qs.discount_amount
                    final_cart_qs.coupon = coupon_qs
                    final_cart_qs.save()
                    return Response({
                        "success": "OK",
                        "msg": "Coupone added successfully"
                    }, status=status.HTTP_200_OK)
            else:
                print("Cannot add more than one coupon")
                return Response({
                    "msg": "Cannot add more than one coupon"
                }, status=status.HTTP_400_BAD_REQUEST)
        else:
            print("Invalid Coupon")
            return Response({
                "msg": "Invalid Coupon"
            }, status=status.HTTP_400_BAD_REQUEST)
