from django.urls import path

from .views import OrderCreateApiVew, SslCommerzTest, CreateTest, OrdercofirmApiView

urlpatterns = [
    path("create-order", OrderCreateApiVew.as_view()),
    path("ssl-payment", SslCommerzTest.as_view()),
    path("order-confirm", OrdercofirmApiView.as_view()),
    path("test", CreateTest.as_view())
]
