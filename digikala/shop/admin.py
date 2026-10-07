from django.contrib import admin

from . import models


admin.site.register(models.Category)


class AddressInline(admin.StackedInline):
    model = models.Address
    extra = 0


class CustomerAdmin(admin.ModelAdmin):
    inlines = [AddressInline]


admin.site.register(models.Customer, CustomerAdmin)


admin.site.register(models.Product)

admin.site.register(models.Order)
