from django.contrib import admin
from django.urls import path

from .views import *

from rest_framework import routers

router = routers.SimpleRouter()

router.register('clients', ClientViewSet, basename='clients')
router.register('restaurants', RestaurantViewSet, basename='restaurants')
router.register('couriers', CourierViewSet, basename='couriers')
router.register('regions', RegionViewSet, basename='regions')
router.register('menu_item', MenuItemViewSet, basename='menu_item')
router.register('order', OrderViewSet, basename='order')
router.register('courier_order', CourierOrderViewSet, basename='courier_order')


urlpatterns = [
                path('', main_page),
                path('admin/', admin.site.urls),
                path('hello/', hello),
                path('info/', InfoView.as_view()),
                path('menu/', MenuView.as_view()),
                path('authorization/', authorization),
                path('login/', LoginView),
                path('', login)
              ] + router.urls
