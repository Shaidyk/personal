from django.db import models
from .region import Region


class Client(models.Model):
    """Client"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    prefer_region = models.ForeignKey(Region,
                                      on_delete=models.CASCADE,
                                      null=True)
    phone = models.PositiveIntegerField()

    def __str__(self):
        return f"Client name: {self.first_name}. Phone: {self.phone}"
