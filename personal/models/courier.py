from django.db import models
from .region import Region


class Courier(models.Model):
    """Courier"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.PositiveIntegerField(null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return "Courier name - {}, Courier last name - {}. Region: {}".format(
            self.first_name,
            self.last_name,
            self.region)
