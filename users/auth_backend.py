from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.contrib.auth import get_user_model

User = get_user_model()


class EmailOrPhoneBackend(ModelBackend):
    def authenticate(self, username, phone_number=None, email=None, otp=None,  password=None, **kwargs):
        print('custom backend', self)
        print('otp', otp)
        try:
            user = User.objects.get(
                Q(phone_number=phone_number) | Q(email=email))
            if user:
                print(user)
        except User.DoesNotExist:
            print('error')
        return None

    def get_user(self, uid):
        try:
            return User.objects.get(pk=uid)
        except User.DoesNotExist:
            return None
