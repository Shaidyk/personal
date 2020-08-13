from django.db import models


class Client(models.Model):
    """Client"""
    first_name = models.CharField(max_length=100)
    phone = models.PositiveIntegerField()

    def __str__(self):
        return f"Client name: {self.first_name}. Phone: {self.phone}"


class Region(models.Model):
    """Region"""
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    """Restaurant"""
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return f"Restaurant: {self.name}. Region:{self.region}"


class Courier(models.Model):
    """Courier"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return f"Courier name: {self.first_name}, Courier last name - {self.last_name}"


class Category(models.Model):
    """Category"""
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    """Position in menu"""
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    # currency = models.CharField(max_length=10, default="₴")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.category}: {self.name}. {self.price}₴"


class Order(models.Model):
    """Order"""
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    delivery_time = models.DateTimeField()
    delivered_at = models.DateTimeField()

    def __str__(self):
        return f"{self.client}, {self.restaurant}, {self.courier}"


class OrderItem(models.Model):
    """Position menu in order"""
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)  # count

    def __str__(self):
        return f"Menu Item{self.menuitem}. Order = {self.order}. Amount{self.amount}"
