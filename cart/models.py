from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, pre_delete
from django.utils import timezone

from products.models import Products, Variants, Size
from coupon.models import Coupon

User = settings.AUTH_USER_MODEL


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    variant = models.ForeignKey(
        Variants, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0)
    expires = models.BooleanField(blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f"{self.user.phone_number} ordered {self.quantity} pcs of {self.product.name}"


class FinalCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ManyToManyField(Cart)
    expires = models.BooleanField(default=False)
    coupon = models.CharField(max_length=40, blank=True, null=True)
    sub_total = models.PositiveIntegerField(default=1)
    total = models.PositiveBigIntegerField(default=1)
    coupon = models.ForeignKey(
        Coupon, on_delete=models.CASCADE, blank=True, null=True
    )
    total_saved = models.PositiveBigIntegerField(default=0)
    expires = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now())
    ordered_date = models.DateTimeField()

    def __str__(self) -> str:
        return f"{self.user.phone_number} ordered"
