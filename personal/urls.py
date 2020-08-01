from django.contrib import admin
from django.urls import path

from .views import hello, InfoView, main_page, MenuView

urlpatterns = [
    path('', main_page),
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('info/', InfoView.as_view()),
    path('menu/', MenuView.as_view()),
]
