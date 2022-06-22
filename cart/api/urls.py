from django.urls import path

from .views import (
    AddToCart,
    CheckCanAddToCart,
    UserCartListApiView,
    PlusQuantity,
    MinusQuantity,
    CouponAddedApi
)

urlpatterns = [
    path('add-to-cart', AddToCart.as_view()),
    path('check-add-to-cart', CheckCanAddToCart.as_view()),
    path("cart-list", UserCartListApiView.as_view()),
    path("plus-quantity", PlusQuantity.as_view()),
    path("minus-quantity", MinusQuantity.as_view()),
    path("coupon-add", CouponAddedApi.as_view()),
]
