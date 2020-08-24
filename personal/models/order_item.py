from django.db import models
from .menu_item import MenuItem
from .order import Order


class OrderItem(models.Model):
    """Position menu in order"""
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)  # count

    def __str__(self):
        return f"Menu Item{self.menuitem}. Order = {self.order}. Amount{self.amount}"
