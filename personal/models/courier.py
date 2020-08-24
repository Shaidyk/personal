from django.db import models
from .region import Region


class Courier(models.Model):
    """Courier"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return f"Courier name - {self.first_name}, Courier last name - {self.last_name}. Region: {self.region}"
