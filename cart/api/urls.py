from django.urls import path

from .views import AddToCart, CheckCanAddToCart

urlpatterns = [
    path('add-to-cart', AddToCart.as_view()),
    path('check-add-to-cart', CheckCanAddToCart.as_view())

]
