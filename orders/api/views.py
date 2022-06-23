from django.utils import timezone

from rest_framework import views, generics, status
from rest_framework.response import Response

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
                    order_status='ceated'
                )
                return Response(status=status.HTTP_200_OK)
        else:
            return Response({
                "msg": "No active cart found"
            }, status=status.HTTP_400_BAD_REQUEST)
