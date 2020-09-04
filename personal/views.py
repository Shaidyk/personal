from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.shortcuts import render
import datetime

from .serializers import *
from .models import *
from .permissions import *

from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.decorators import api_view, permission_classes


class MenuView(TemplateView):
    template_name = "menu.html"

    def get(self, request, *args, **kwargs):
        context = {"menu_items": []}

        queryset = MenuItem.objects.all()
        categories = Category.objects.all()

        for category in categories:
            items = queryset.filter(category=category).order_by('price')
            items = list(items)
            if items != []:
                result = {
                    'name': category,
                    'items': items
                }
                context['menu_items'].append(result)

        return render(request, self.template_name, context)


def hello(request):
    return HttpResponse(
        """
        <html>
            <body>
                <p style="color: red"> Hello Django!!! </p>
                <a style="background-color: yellow" href="/"> Main-page </a>
            </body>
        </html>
        """)


class InfoView(TemplateView):
    template_name = "info.html"

    def get(self, request, *args, **kwargs):
        context = {
            "info_times": datetime.datetime.now().strftime("%d %b %Y, %H:%M:%S")
        }
        return render(request, self.template_name, context)


def main_page(request):
    return render(request, "main.html")


def authorization(request):
    return render(request, "login.html")


# @api_view(['GET'])
# @permission_classes([CanConfirmOrder & CanCompleteOrder])
def LoginView(request, format=None):
    return HttpResponseRedirect('/')


def login(request):
    return render(request, "main.html")


class ClientViewSet(ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class RestaurantViewSet(ReadOnlyModelViewSet):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()


class CourierViewSet(ModelViewSet):
    serializer_class = CourierSerializer
    queryset = Courier.objects.all()


class RegionViewSet(ModelViewSet):
    serializer_class = RegionSerializer
    queryset = Region.objects.all()


class MenuItemViewSet(ReadOnlyModelViewSet):
    serializer_class = MenuItemSerializer
    queryset = MenuItem.objects.all()


class OrderViewSet(ReadOnlyModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class CourierOrderViewSet(ModelViewSet):
    serializer_class = CourierOrderSerializer
    queryset = Order.objects.all()
