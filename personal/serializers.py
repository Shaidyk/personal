from rest_framework import serializers

from .models import Client, Restaurant, Courier, Region, MenuItem


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
