from rest_framework.viewsets import ModelViewSet

from ..serializers import RegionSerializer
from ..models import Region


class RegionViewSet(ModelViewSet):
    serializer_class = RegionSerializer
    queryset = Region.objects.all()