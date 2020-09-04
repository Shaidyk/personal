from rest_framework.viewsets import ModelViewSet

from ..serializers import CourierSerializer
from ..models import Courier


class CourierViewSet(ModelViewSet):
    serializer_class = CourierSerializer
    queryset = Courier.objects.all()