import code
from itertools import product
from turtle import color
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from taggit.managers import TaggableManager

from django.contrib.auth import settings

User = settings.AUTH_USER_MODEL

STATUS = (
    ('TRUE', 'TRUE'),
    ('FALSE', 'FALSE'),
)

PRODUCT_DISPLAY_VARIANT = (
    ('None', 'None'),
    ('Size', 'Size'),
    ('Color', 'Color'),
    ('Size-Color', 'Size-Color'),
)


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, null=True)
    keywords = TaggableManager()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/category', blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(
        max_length=100,
        help_text='The name of the product',
    )
    '''
        Supplier details information
        need to be store when create any
        particular product
    '''
    supplier_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text='Supplier Profile'
    )
    slug = models.SlugField(
        blank=True, null=True,
        help_text='Do not put anything in this field'
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    short_description = models.CharField(
        max_length=80,
        help_text='A short description for the product within 80 words'
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    keywords = TaggableManager()
    thumbnail = models.ImageField(
        upload_to='images/products',
        blank=True
    )
    price = models.PositiveIntegerField(
        default=10,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(1000000)
        ],
        help_text='Price must have to be in between 0-1000000'
    )
    variant = models.CharField(
        max_length=20,
        choices=PRODUCT_DISPLAY_VARIANT,
        default='None',
        help_text='Based on this product will show in details page'
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default='TRUE'
    )
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name


class ProductImages(models.Model):
    product = models.ForeignKey(
        Products,
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to='images/products'
    )
    alt_text = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text='This text will show if the picture not able to load properly'
    )

    class Meta:
        verbose_name_plural = 'Product Images'

    def __str__(self):
        return self.product.name


class Color(models.Model):
    name = models.CharField(
        max_length=14,
        blank=True,
        null=True,
    )
    code = models.CharField(
        max_length=10,
        help_text='This will be the color code of this product'
    )

    class Meta:
        verbose_name_plural = 'Colors'

    def __str__(self):
        return self.code


class Size(models.Model):
    name = models.CharField(
        max_length=14,
        blank=True,
        null=True,
    )
    code = models.CharField(
        max_length=10,
        help_text='This will be the size code of this product'
    )

    def __str__(self):
        return self.code


class Variants(models.Model):
    title = models.CharField(
        max_length=20,
        blank=True,
        null=True,
    )
    product = models.ForeignKey(
        Products,
        on_delete=models.CASCADE
    )
    color = models.ForeignKey(
        Color,
        on_delete=models.CASCADE
    )
    size = models.ForeignKey(
        Size,
        on_delete=models.CASCADE
    )
    image_id = models.CharField(
        max_length=5,
        blank=True,
        null=True,
    )
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField(
        default=10,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(1000000)
        ],
        help_text='Price must have to be in between 0-1000000'
    )

    def __str__(self) -> str:
        return self.product.name