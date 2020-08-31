from django.db import models
from .client import Client
from .restaurant import Restaurant
from .courier import Courier


class Order(models.Model):
    """Order"""
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    courier = models.ForeignKey(Courier,
                                related_name='orders',
                                on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    delivery_time = models.DateTimeField()
    delivered_at = models.DateTimeField()
    status = models.CharField(max_length=20,
                              choices=(('CREATED', 'CREATED'),
                                       ('CONFIRMED', 'CONFIRMED'),
                                       ('IN PROGRESS', 'IN PROGRESS'),
                                       ('DELIVERING', 'DELIVERING'),
                                       ('COMPLETED', 'COMPLETED')),
                              null=True)

    def __str__(self):
        return f"{self.client}, {self.restaurant}, {self.courier}"
