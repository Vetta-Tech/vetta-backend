from django.db import models
from django.db.models.signals import pre_save
from django.conf import settings

from address.models import Address
from cart.models import FinalCart

from .utils import unique_order_id_generator

User = settings.AUTH_USER_MODEL

ORDER_STATUS = (
    ('ceated', 'ceated'),
    ('confirmed', 'confirmed'),
    ('order_processing', 'order_processing'),
    ('delivery_started', 'delivery_started'),
    ('delivery_completed', 'delivery_completed'),
    ('delivery_cancelled', 'delivery_cancelled'),
)


PAYMENT_METHOD = (
    ('COD', 'COD'),
    ('CARD', 'CARD'),
    ('MFS', 'MFS'),
)


class Order(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    order_id = models.CharField(
        max_length=20, blank=True, null=True
    )
    final_cart = models.ForeignKey(
        FinalCart, on_delete=models.CASCADE
    )

    shipping_charge = models.PositiveIntegerField(default=60)
    order_sub_total = models.PositiveIntegerField(default=1)
    order_total = models.PositiveIntegerField(default=1)

    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=20)

    order_status = models.CharField(
        max_length=64, blank=True, null=True, choices=ORDER_STATUS)

    orordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField()

    def __str__(self) -> str:
        return self.order_id


class PaymentInfo(models.Model):
    order_number = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    tran_id = models.CharField(max_length=15)
    val_id = models.CharField(max_length=75)
    card_type = models.CharField(max_length=150)
    store_amount = models.DecimalField(max_digits=10, decimal_places=2)
    card_no = models.CharField(max_length=55, null=True)
    bank_tran_id = models.CharField(max_length=155, null=True)
    status = models.CharField(max_length=55)
    tran_date = models.DateTimeField()
    currency = models.CharField(max_length=10)
    card_issuer = models.CharField(max_length=255)
    card_brand = models.CharField(max_length=15)
    card_issuer_country = models.CharField(max_length=55)
    card_issuer_country_code = models.CharField(max_length=55)
    currency_rate = models.DecimalField(max_digits=10, decimal_places=2)
    verify_sign = models.CharField(max_length=155)
    verify_sign_sha2 = models.CharField(max_length=255)
    risk_level = models.CharField(max_length=15)
    risk_title = models.CharField(max_length=25)


def pre_save_create_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = unique_order_id_generator(instance)


pre_save.connect(pre_save_create_order_id, sender=Order)
