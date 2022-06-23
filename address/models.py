from django.db import models
from django.utils import timezone
from django.conf import settings

User = settings.AUTH_USER_MODEL

ADDRESS_COICES = (
    ('Home', 'Home'),
    ('Office', 'Office'),
)


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lattitude = models.CharField(max_length=6, blank=True, null=True)
    longtitude = models.CharField(max_length=6, blank=True, null=True)
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

    def __str__(self) -> str:
        return self.lattitude
