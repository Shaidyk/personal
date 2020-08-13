from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render
import datetime
from .models import Category, MenuItem

from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .serializers import ClientSerializer, RestaurantSerializer, CourierSerializer, RegionSerializer, MenuItemSerializer
from .models import Client, Restaurant, Courier, Region


class MenuView(TemplateView):
    template_name = "menu.html"

    def get(self, request, *args, **kwargs):
        context = {"menu_items": []}

        queryset = MenuItem.objects.all()
        categories = Category.objects.all()

        for category in categories:
            items = queryset.filter(category=category).order_by('price')
            result = {
                'name': category,
                'items': list(items)
            }
            context['menu_items'].append(result)

        # filter_name = request.GET.get("filter")
        # if filter_name:
        #     queryset = queryset.filter(name__contains=filter_name)

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


class ClientViewSet(ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class RestaurantViewSet(ReadOnlyModelViewSet):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()


class CourierViewSet(ReadOnlyModelViewSet):
    serializer_class = CourierSerializer
    queryset = Courier.objects.all()


class RegionViewSet(ReadOnlyModelViewSet):
    serializer_class = RegionSerializer
    queryset = Region.objects.all()


class MenuItemViewSet(ReadOnlyModelViewSet):
    serializer_class = MenuItemSerializer
    queryset = MenuItem.objects.all()
