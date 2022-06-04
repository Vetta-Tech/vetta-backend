from django.db import models
from django.conf import settings
from django.utils import timezone

from products.models import Products, Variants

User = settings.AUTH_USER_MODEL


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    variant = models.ForeignKey(Variants, on_delete=models.CASCADE)
    size = models.CharField(max_length=20, blank=True, null=True)
    color = models.CharField(max_length=20, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f"{self.user.phone_number} ordered {self.quantity} pcs of {self.product.name}"


class FinalCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ManyToManyField(Cart)
    expires = models.BooleanField(default=False)
    coupon = models.CharField(max_length=40, blank=True, null=True)
    sub_total = models.PositiveIntegerField(default=1)

    created_at = models.DateTimeField(default=timezone.now())
    ordered_date = models.DateTimeField()

    def __str__(self) -> str:
        return f"{self.user.phone_number} ordered"
