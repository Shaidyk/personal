from django.db import models
import datetime


class Client(models.Model):
    first_name = models.CharField(max_length=100)
    phone = models.PositiveIntegerField()


class Region(models.Model):
    name = models.CharField(max_length=200)


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)


class Courier(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)


class MenuItem(models.Model):
    name = models.CharField(max_length=150)
    price = models.TextField(max_length=1000)


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    delivery_time = models.DateTimeField()
    delivered_at = models.DateTimeField()


class OrderItem(models.Model):
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
