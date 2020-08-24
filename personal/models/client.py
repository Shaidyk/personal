from django.db import models


class Client(models.Model):
    """Client"""
    first_name = models.CharField(max_length=100)
    phone = models.PositiveIntegerField()

    def __str__(self):
        return f"Client name: {self.first_name}. Phone: {self.phone}"
