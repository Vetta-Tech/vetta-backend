import os

import firebase_admin
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from firebase_admin import auth
from firebase_admin import credentials
from rest_framework import authentication
from rest_framework import exceptions

from .exceptions import FirebaseError
from .exceptions import InvalidAuthToken
from .exceptions import NoAuthToken

cred = credentials.Certificate(
    {
        "type": "service_account",
        "project_id": "socialapp-5005d",
        "private_key_id": "40d6018294982f1c14ba2e530e5961fdf0fb8de9",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC6EA5A5YC14V/M\n780L+Er7jJajL6jJNkJJH0WYibhIuhGM28kOVT6CFVe0AwT742Cs71+wDAGK1v7V\nTrAwawdLpVMn+vlRfaiDQeWCS8oBV520cdhjY02MjEsEsmd6Plapw5o+S0xS7T5c\n3W+23VwqVYXS/kY1bqeW8sfWJCzuEub01+xuaYOx/L1qeYNwLgdsrvp4kp0DnVQL\no4H93Qzc5bNXkrHxK7Eia+Sdm6KFu0X0IOKm+GCFbP5fHR1f0yMuEfR3aUMz8GTt\nyYQ3i/ukvVzU4x2e+wmdcDsBB/yUeFN0n31HvY0ST1xcPpJzvcopErlYldK/vknZ\nZQM/pVMtAgMBAAECggEAUHbdEyetT/rVaVVTQZfxJXQZOR1FSy8R33mMqXj1n04I\nhPgPrQkkbTE5qnmb0Cr3BhLHOOUYTajIsArFm0rN7uLiYWniJGHJXGpFDOIlzArO\nAtkxEVpCkUOitbdJlM4cwHH85G+/5CUBUTvaMiTs1MoDg8m/JyBhjaAU2ADxBUue\ndnQBsUIXTaqTTrRvhcYyxI4w+zSFoibr+V9+Gb6MgseKSrcfjXkchYBRMG5lUnUK\njwneD2RQJNOZ715XuC/SXXszuofMdWK4S4mBTTp83BNU6/MXqttGBcKpiYdjjufx\nPMBdNrsZvwAgaE5JWjqpEATG1Si3/didWU2Fh3NeaQKBgQDjIxU3IRpYU0vRrHIq\nbrIpAcnycEYhQosbgmk+KRYejFzfQlbxCJBbiyBz6+z1icC2fNkXZ/DWAEKvID31\naK8YZ93+BZ9+F5sTexx6BA0SilyrNZbhnQqsY7TWuuMoHhn0HjllqHxyAE1DRvX0\nkTV/Gxaj5BVbHVaZZiJWMw7+HwKBgQDRtMxMqGCPnXfhc6ObwRo9hfcsQiEn49wG\nRsDDnLu/D/zQhZXXcsxqyzljEPYSMfQxPOPrm4BKy15P3n35bM18xWTaly/moPTR\nRiW5lpWit2piwbYr4D00er3x+YDl0fsoZTc7WEq66LsNriA58b45SmCuMh3k2cTb\nqaDgtNrtMwKBgQCCwrK2/y6shJ+UgONkvD+Czg3VrX8iLK3q02QFLiAWzBW3TfjB\nYH3CxdCUC9Fp9bjlFfDgwazrdlDtgvFIc9DBiyJI2DHepHZZe7mEIQrpjpAU3JAV\nKJR5dBkquYKGmPW2DSRb+uhRtQzF23dDKcmTeCPLjEYjIzu0qhDAcTqDXwKBgAkB\n6hCU3ujsS5zseaeUCMuBuJc3E/OBrw659UexsMLJLgPK6R/C95LSvdlKfjdT2/hN\ndEDHgiA0Ug2+Mc0H5l+onudgvRb77OgcSjyJgk3l8PTi+y8xR4+8gfIl1GqKtW4L\nwu6SoUsb+gThaNL0VkZhsnto/a25yOHijF16hzjPAoGBANYryDfm/Jkgj4EjvFQ8\nThj0BWb+ZQRyERVfXcfGUUqgZ8F3WZvpMhJ/5KA0G0WVzHy4qcSpC42LpknTFz7E\nxRKRI8BQjPTQI347ixrHM6/4mV3enE9xtEgZygansPFEvUR5wrMNE+cHTQ7ABhtt\nkA3hSkR3s8MXOOUAru/60ltU\n-----END PRIVATE KEY-----\n",
        "client_email": "firebase-adminsdk-wpqnu@socialapp-5005d.iam.gserviceaccount.com",
        "client_id": "100785713391028071719",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-wpqnu%40socialapp-5005d.iam.gserviceaccount.com"
    }
)

default_app = firebase_admin.initialize_app(cred)


class FirebaseAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get("HTTP_AUTHORIZATION")
        print(auth_header)
        if not auth_header:
            raise NoAuthToken("No auth token provided")

        id_token = auth_header.split(" ").pop()
        decoded_token = None
        try:
            decoded_token = auth.verify_id_token(id_token)
        except Exception:
            raise InvalidAuthToken("Invalid auth token")
            pass

        if not id_token or not decoded_token:
            return None

        try:
            uid = decoded_token.get("uid")
        except Exception:
            raise FirebaseError()

        user, created = User.objects.get_or_create(username=uid)
        user.profile.last_activity = timezone.localtime()

        return (user, None)
