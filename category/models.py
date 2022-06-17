from django.db import models
from django.utils import timezone

from taggit.managers import TaggableManager

STATUS = (
    ('TRUE', 'TRUE'),
    ('FALSE', 'FALSE'),
)


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, null=True)
    keywords = TaggableManager()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/category', blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='TRUE')
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=True, null=True)
    keywords = TaggableManager()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='image/subcategory', blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='TRUE')
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'Subcategory'

    def __str__(self):
        return self.name
