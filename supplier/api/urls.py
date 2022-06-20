from django.urls import path

from .views import HomeSupplierList, SupplierDetails, SupplierProductsByCategory, SupplierByCategory

urlpatterns = [
    path('brand-list', SupplierByCategory.as_view()),
    path('brand-details', SupplierProductsByCategory.as_view()),
    path('', HomeSupplierList.as_view()),
    path('<slug>', SupplierDetails.as_view()),
]
