from django.db import models
from django.core.validators import MinValueValidator

from .category import Category
from .menu import Menu


class MenuItem(models.Model):
    """Position in menu"""
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                null=True,
                                validators=[MinValueValidator(0.01)])
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    menu = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.category}: {self.name}. {self.price}₴"
