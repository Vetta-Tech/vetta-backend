from django.contrib import admin

from .models import (

    Products,
    ProductImages,
    Color,
    Size,
    Variants,
)


class ProductsImagesAdmin(admin.StackedInline):
    model = ProductImages


class VariantsAdmin(admin.StackedInline):
    model = Variants


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductsImagesAdmin, VariantsAdmin]

    class Meta:
        model = Products


admin.site.register(Variants)
admin.site.register(ProductImages)
admin.site.register(Color)
admin.site.register(Size)
