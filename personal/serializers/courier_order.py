from rest_framework import serializers

from ..models import Order, Client
from . import ClientSerializer, RestaurantSerializer


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