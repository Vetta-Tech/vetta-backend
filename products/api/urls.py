from django.urls import path

from .views import (
    ProductListApiView,
    ProductDetailsApiView,
    HomeProductsApiView,
    FetchProductsByCategory,
    GetProductsByBrands,
    GetAllCategories,
    GetFeaturedProducts
)

urlpatterns = [
    path('', ProductListApiView.as_view()),
    path('home', HomeProductsApiView.as_view()),
    path('details/<slug>', ProductDetailsApiView.as_view()),
    path('category/products', FetchProductsByCategory.as_view()),
    path('brands', GetProductsByBrands.as_view()),
    path('categories', GetAllCategories.as_view()),
    path('featured-infinite', GetFeaturedProducts.as_view()),
]
