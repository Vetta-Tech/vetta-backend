from django.urls import path

from .views import CheckPhoneNumberValidOrNot, GenerateOtp, ValidateOtp

urlpatterns = [
    path('is-phone-number-valid', CheckPhoneNumberValidOrNot.as_view()),
    path('generate-otp', GenerateOtp.as_view()),
    path('validate-otp', ValidateOtp.as_view()),
]
