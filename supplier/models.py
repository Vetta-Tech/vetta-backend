from django.db import models

from category.models import Category


class Supplier(models.Model):
    name = models.CharField(
        max_length=20
    )
    slug = models.SlugField(
        blank=True,
        null=True
    )
    descrition = models.TextField(
        max_length=300,
        blank=True,
        null=True
    )
    logo = models.ImageField(
        upload_to='images/brand/logo'
    )
    cover_image = models.ImageField(
        upload_to='images/brand/cover'
    )
    category = models.ManyToManyField(Category)
    active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self) -> str:
        return self.name
