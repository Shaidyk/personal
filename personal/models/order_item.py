from django.db import models
from django.core.validators import MinValueValidator

from .menu_item import MenuItem
from .order import Order


class OrderItem(models.Model):
    """Position menu in order"""
    menuitem = models.ForeignKey(MenuItem, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.FloatField(default=0,
                               validators=[MinValueValidator(0.01)])  # count

    def __str__(self):
        return "Menu Item{}. Order = {}. Amount{}".format(self.menuitem,
                                                          self.order,
                                                          self.amount)
