from django.urls import path

from .views import (
    ProductListApiView,
    ProductDetailsApiView,
    HomeProductsApiView,
    FetchProductsByCategory
)

urlpatterns = [
    path('', ProductListApiView.as_view()),
    path('home', HomeProductsApiView.as_view()),
    path('details/<slug>', ProductDetailsApiView.as_view()),
    path('category/products', FetchProductsByCategory.as_view())
]
