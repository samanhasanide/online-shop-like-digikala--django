from django.contrib import admin

from .models import Product, Category, ProductImage

from . import models


admin.site.register(models.Category)


class AddressInline(admin.StackedInline):
    model = models.Address
    extra = 0


class CustomerAdmin(admin.ModelAdmin):
    inlines = [AddressInline]


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]


admin.site.register(models.Customer, CustomerAdmin)

admin.site.register(models.Order)
