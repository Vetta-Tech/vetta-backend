from django.urls import path

from .views import OrderCreateApiVew, SslCommerzTest

urlpatterns = [
    path("create-order", OrderCreateApiVew.as_view()),
    path("ssl-payment", SslCommerzTest.as_view())
]
