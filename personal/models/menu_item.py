from django.db import models
from .category import Category


class MenuItem(models.Model):
    """Position in menu"""
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    # currency = models.CharField(max_length=10, default="₴")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.category}: {self.name}. {self.price}₴"