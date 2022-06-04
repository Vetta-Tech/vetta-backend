from django.urls import path

from .views import (
    ProductListApiView,
    ProductDetailsApiView
)

urlpatterns = [
    path('', ProductListApiView.as_view()),
    path('details/<slug>', ProductDetailsApiView.as_view())

]
