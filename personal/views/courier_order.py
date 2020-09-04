from rest_framework.viewsets import ModelViewSet

from ..serializers import CourierOrderSerializer
from ..models import Order


class CourierOrderViewSet(ModelViewSet):
    serializer_class = CourierOrderSerializer
    queryset = Order.objects.all()
