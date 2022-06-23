import datetime
from django.conf import settings
from rest_framework import views, status, generics
from rest_framework.response import Response
from proman_phone_login.models import PhoneToken

from proman_phone_login.serializers import PhoneTokenCreateSerializer, PhoneTokenValidateSerializer
from users.models import User

UserOne = settings.AUTH_USER_MODEL


class CheckPhoneNumberValidOrNot(views.APIView):
    def get(self, request, *args, **kwargs):
        user = request.user

        print(user.is_phone_verified)
        if user.is_authenticated:
            if user.is_phone_verified == True:
                return Response({
                    "is_phone_verified": user.is_phone_verified
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "is_phone_verified": user.is_phone_verified
                }, status=status.HTTP_200_OK)
        else:
            return Response({
                "error": "Unauthorized Request"
            }, status=status.HTTP_400_BAD_REQUEST)


class GenerateOtp(generics.CreateAPIView):
    serializer_class = PhoneTokenCreateSerializer
    queryset = PhoneToken.objects.all()

    def post(self, request, *args, **kwargs):
        phone_number = request.data.get('phone_number')
        phone_number_format = phone_number
        print(phone_number_format)
        user_qs = User.objects.filter(phone_number=str(phone_number_format))
        print(user_qs)
        if not user_qs:
            ser = self.serializer_class(
                data=request.data,
                context={'request': request}
            )

            if ser.is_valid():
                token = PhoneToken.create_otp_for_number(
                    request.data.get('phone_number')
                )
                if token:
                    phone_token = self.serializer_class(
                        token, context={'request': request}
                    )
                    return Response(phone_token.data)
                return Response({
                    'reason': "you can not have more than {n} attempts per day, please try again tomorrow".format(
                        n=getattr(settings, 'PHONE_LOGIN_ATTEMPTS', 100))}, status=status.HTTP_400_BAD_REQUEST)
            return Response(
                {'reason': 'Enter a valid phone number'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                {'reason': "Phone already registered"}, status=status.HTTP_400_BAD_REQUEST)


class ValidateOtp(generics.CreateAPIView):
    serializer_class = PhoneTokenValidateSerializer
    queryset = PhoneToken.objects.all()

    def post(self, request, *args, **kwargs):
        ser = self.serializer_class(
            data=request.data, context={'request': request}
        )
        if ser.is_valid():
            pk = request.data.get("pk")
            otp = request.data.get("otp")
            phone_number = request.data.get("phone_number")
            print(phone_number)
            timestamp_difference = datetime.datetime.now() - datetime.timedelta(
                minutes=getattr(settings, 'PHONE_LOGIN_MINUTES', 10)
            )
            phone_token = PhoneToken.objects.get(
                pk=pk,
                otp=otp,
                used=False,
                timestamp__gte=timestamp_difference
            )
            if phone_token:
                user = request.user
                user.is_phone_verified = True
                user.phone_number = '+880'+phone_number
                user.save()
                return Response({
                    "success": "OK"
                }, status=status.HTTP_200_OK)

            else:
                phone_token = PhoneToken.objects.get(pk=pk)
                phone_token.attempts = phone_token.attempts + 1
                phone_token.save()
                return Response({
                    "reason": "Invalid OTP"
                }, status=status.HTTP_400_BAD_REQUEST)
