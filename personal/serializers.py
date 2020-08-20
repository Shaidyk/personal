from rest_framework import serializers

from .models import *


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        # fields = ('id', 'first_name', 'last_name')
        # exclude = ('created', 'changed')
        fields = '__all__'


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class CourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = '__all__'


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    restaurant = RestaurantSerializer()

    class Meta:
        model = Order
        fields = ('client', 'restaurant', 'courier', 'created', 'delivery_time', 'delivered_at')


class OrdersCourierSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    restaurant = RestaurantSerializer()

    class Meta:
        model = Order
        # exclude = ['courier']
        fields = '__all__'


class CourierOrderSerializer(serializers.ModelSerializer):
    orders = OrdersCourierSerializer(many=True)

    class Meta:
        model = Client
        # fields = '__all__'
        fields = ['orders', 'first_name']
