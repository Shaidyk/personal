from django.contrib import admin
from django.urls import path

from .views import hello, InfoView, main_page, MenuView, ClientViewSet, RestaurantViewSet, CourierViewSet, \
    RegionViewSet, MenuItemViewSet

from rest_framework import routers

router = routers.SimpleRouter()

router.register('clients', ClientViewSet, basename='clients')
router.register('restaurants', RestaurantViewSet, basename='restaurants')
router.register('couriers', CourierViewSet, basename='couriers')
router.register('regions', RegionViewSet, basename='regions')
router.register('menu_item', MenuItemViewSet, basename='menu_item')

urlpatterns = [
                  path('', main_page),
                  path('admin/', admin.site.urls),
                  path('hello/', hello),
                  path('info/', InfoView.as_view()),
                  path('menu/', MenuView.as_view()),
              ] + router.urls
