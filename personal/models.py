from django.db import models
import datetime


class Client(models.Model):
    """Клиент"""
    first_name = models.CharField(max_length=100)
    phone = models.PositiveIntegerField()


class Region(models.Model):
    """Район"""
    name = models.CharField(max_length=200)


class Restaurant(models.Model):
    """Ресторан"""
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)


class Courier(models.Model):
    """Курьер"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)


class MenuItem(models.Model):
    """Позиция в меню"""
    name = models.CharField(max_length=150)
    price = models.DecimalField(decimal_places=2)  # цена


class Order(models.Model):
    """Закакз"""
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    delivery_time = models.DateTimeField()
    delivered_at = models.DateTimeField()


class OrderItem(models.Model):
    """Позиция меню в заказе"""
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.FloatField()  # цена
