from rest_framework.viewsets import ReadOnlyModelViewSet

from ..serializers import OrderSerializer
from ..models import Order


class OrderViewSet(ReadOnlyModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
