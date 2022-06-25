import requests
from django.db import models
from django.db.models.signals import pre_save
from django.conf import settings
from django.utils import timezone


from django.db.models.signals import pre_save

User = settings.AUTH_USER_MODEL

ADDRESS_COICES = (
    ('Home', 'Home'),
    ('Office', 'Office'),
)


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lattitude = models.FloatField()
    longtitude = models.FloatField()
    address = models.TextField(
        max_length=200, blank=True,
        null=True
    )

    special_instruction = models.TextField(
        max_length=150, blank=True, null=True)

    address_coices = models.CharField(
        max_length=20, choices=ADDRESS_COICES, blank=True, null=True)

    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(default=timezone.now())


def pre_save_address_fetch(sender, instance, *args, **kwargs):
    if not instance.address:
        res = requests.get(
            "https://barikoi.xyz/v1/api/search/reverse/{BARIKOI_API}/geocode?longitude={lng}&latitude={lat}&district=true&post_code=true&country=true&sub_district=true&union=true&pauroshova=true&location_type=true&division=true&address=true&area=true".format(
                BARIKOI_API=getattr(settings, "BARIKOI_API"),
                lng=instance.longtitude,
                lat=instance.lattitude
            )
        )

        data = res.json()
        formatted_address = data["place"]
        instance.address = formatted_address["address"]


pre_save.connect(pre_save_address_fetch, sender=Address)
