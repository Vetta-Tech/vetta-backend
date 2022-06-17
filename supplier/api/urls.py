from django.urls import path

from .views import HomeSupplierList

urlpatterns = [
    path('', HomeSupplierList.as_view())
]
