from django.db import models
from .region import Region


class Restaurant(models.Model):
    """Restaurant"""
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return f"Restaurant: {self.name}. Region:{self.region}"
