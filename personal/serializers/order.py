from rest_framework import serializers

from . import ClientSerializer, RestaurantSerializer


class OrderSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    restaurant = RestaurantSerializer()
