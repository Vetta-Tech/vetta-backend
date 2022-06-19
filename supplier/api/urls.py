from django.urls import path

from .views import HomeSupplierList, SupplierDetails, SupplierProductsByCategory

urlpatterns = [
    path('brand-details', SupplierProductsByCategory.as_view()),
    path('', HomeSupplierList.as_view()),
    path('<slug>', SupplierDetails.as_view()),
]
