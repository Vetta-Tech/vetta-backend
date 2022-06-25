from django.utils import timezone

from rest_framework import views, generics, status
from rest_framework.response import Response

from sslcommerz_lib import SSLCOMMERZ

from address.models import Address
from cart.models import FinalCart
from orders.models import Order
from .serializers import OrderSerializer


class OrderCreateApiVew(views.APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        user_fnal_cart_qs = FinalCart.objects.filter(
            user=user,
            expires=False
        ).first()
        user_address_qs = Address.objects.filter(
            user=user
        ).first()

        if user_fnal_cart_qs:
            ordered_date = timezone.now()
            order_qs = Order.objects.filter(
                user=user,
                orordered=False,
                final_cart__id=user_fnal_cart_qs.id
            ).first()
            if order_qs:
                order_qs.order_total = user_fnal_cart_qs.total
                order_qs.save()
                return Response(status=status.HTTP_200_OK)
            else:
                Order.objects.create(
                    user=user,
                    ordered_date=ordered_date,
                    final_cart=user_fnal_cart_qs,
                    order_total=user_fnal_cart_qs.total,
                    order_status='ceated',
                    address=user_address_qs
                )
                return Response(status=status.HTTP_200_OK)
        else:
            return Response({
                "msg": "No active cart found"
            }, status=status.HTTP_400_BAD_REQUEST)


class SslCommerzTest(views.APIView):

    def post(self, request, *args, **kwargs):

        user = request.user
        print(user)
        order_qs = Order.objects.filter(user=user, orordered=False).first()

        order_total = order_qs.order_total
        print(order_total)

        settings = {'store_id': 'proma6135dc6bc8c18',
                    'store_pass': 'proma6135dc6bc8c18@ssl', 'issandbox': True}
        sslcz = SSLCOMMERZ(settings)
        post_body = {}
        # post_body['user'] = user
        post_body['total_amount'] = order_total
        post_body['currency'] = "BDT"
        post_body['tran_id'] = 'asd'
        post_body['success_url'] = 'https://proman.clothing/user/success'
        post_body['fail_url'] = 'https://proman.clothing/user/failure'
        post_body['cancel_url'] = 'https://proman.clothing/user/cancel'
        post_body['emi_option'] = 0
        post_body['cus_name'] = 'sohan'
        post_body['cus_email'] = 'email@rmail.com'
        post_body['cus_phone'] = '8888'
        post_body['cus_add1'] = 'request.data'
        post_body['cus_city'] = 'request.data'
        post_body['cus_country'] = 'Bangladesh'
        post_body['shipping_method'] = "NO"
        post_body['multi_card_name'] = ""
        post_body['num_of_item'] = 1
        post_body['product_name'] = "Test"
        post_body['product_category'] = "Test Category"
        post_body['product_profile'] = "general"
        post_body['value_b'] = order_qs.id
        print(post_body)
        response = sslcz.createSession(post_body)
        print(response)
        return Response(response)
