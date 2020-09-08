from rest_framework.viewsets import ReadOnlyModelViewSet

from ..serializers import MenuItemSerializer
from ..models import MenuItem


class MenuItemViewSet(ReadOnlyModelViewSet):
    serializer_class = MenuItemSerializer
    queryset = MenuItem.objects.all()