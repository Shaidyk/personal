from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return f"{self.name}"
