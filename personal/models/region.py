from django.db import models


class Region(models.Model):
    """Region"""
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'
