from django.contrib.admin import ModelAdmin, register

from . import models


@register(models.Client)
class ClientAdmin(ModelAdmin):
    pass


@register(models.Region)
class RegionAdmin(ModelAdmin):
    pass


@register(models.Restaurant)
class RestaurantAdmin(ModelAdmin):
    pass


@register(models.Courier)
class CourierAdmin(ModelAdmin):
    pass


@register(models.Category)
class CategoryAdmin(ModelAdmin):
    pass


@register(models.MenuItem)
class MenuItemAdmin(ModelAdmin):
    pass


@register(models.Order)
class OrderAdmin(ModelAdmin):
    pass


@register(models.OrderItem)
class OrderItemAdmin(ModelAdmin):
    pass
