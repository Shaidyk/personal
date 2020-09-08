from django.db import models


class Category(models.Model):
    """Category"""
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.name}'
