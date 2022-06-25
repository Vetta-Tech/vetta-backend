from django.urls import path

from .views import CreateAddressApiView, AddressEditView, GetUserAddress, SaveLocalCoordsToDB

urlpatterns = [
    path('user-address', GetUserAddress.as_view()),
    path('save-local-address', SaveLocalCoordsToDB.as_view()),
    path("create-address", CreateAddressApiView.as_view()),
    path('edit/<id>', AddressEditView.as_view()),
]
