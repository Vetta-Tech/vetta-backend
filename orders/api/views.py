from django.utils import timezone

from rest_framework import views, generics, status
from rest_framework.response import Response

from sslcommerz_lib import SSLCOMMERZ

from address.models import Address
from cart.models import Cart, FinalCart
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

        settings = {'store_id': 'cosme5ff2ce80343e6',
                    'store_pass': 'cosme5ff2ce80343e6@ssl', 'issandbox': True}
        sslcz = SSLCOMMERZ(settings)
        post_body = {}
        # post_body['user'] = user
        post_body['total_amount'] = order_total
        post_body['currency'] = "BDT"
        post_body['tran_id'] = 'asd'
        post_body['success_url'] = 'https://www.youtube.com/'
        post_body['fail_url'] = 'https://m.facebook.com/'
        post_body['cancel_url'] = 'http://192.168.1.110:8000/api/v1/orders/test'
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


class OrdercofirmApiView(views.APIView):
    def post(self, request, *args, **kwargs):
        user = request.user

        payment_method = request.data.get('payment_method', None)
        cart_qs = Cart.objects.filter(user=request.user, expires=False)
        for q in cart_qs:
            q.expires = True
            q.save()
        final_cart_qs = FinalCart.objects.filter(
            user=request.user, expires=False).first()
        if final_cart_qs:
            order_qs = Order.objects.filter(user=user, orordered=False).first()
            if order_qs:
                print('order_qs', order_qs)
                final_cart_qs.expires = True
                final_cart_qs.save()

                order_qs.orordered = True
                order_qs.payment_method = payment_method
                order_qs.save()

                print(order_qs)
                serializer = OrderSerializer(order_qs)
                return Response({'order_qs': serializer.data}, status=status.HTTP_200_OK)
            return Response({'msg': "No active order found"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'msg': "No active cart found"}, status=status.HTTP_400_BAD_REQUEST)


class CreateTest(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
