from rest_framework.viewsets import ReadOnlyModelViewSet

from ..serializers import RestaurantSerializer
from ..models import Restaurant


class RestaurantViewSet(ReadOnlyModelViewSet):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
