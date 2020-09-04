from rest_framework.viewsets import ModelViewSet

from ..serializers import ClientSerializer
from ..models import Client


class ClientViewSet(ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
