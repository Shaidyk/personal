from django.db import models


class Client(models.Model):
    """Client"""
    first_name = models.CharField(max_length=100)
    phone = models.PositiveIntegerField()


class Region(models.Model):
    """Region"""
    name = models.CharField(max_length=200)


class Restaurant(models.Model):
    """Restaurant"""
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)


class Courier(models.Model):
    """Courier"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)


class Category(models.Model):
    """Category"""
    name = models.CharField(max_length=100, null=True)


class MenuItem(models.Model):
    """Position in menu"""
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)


class Order(models.Model):
    """Order"""
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    delivery_time = models.DateTimeField()
    delivered_at = models.DateTimeField()


class OrderItem(models.Model):
    """Position menu in order"""
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)  # count


