from django.contrib import admin
from django.urls import path

from .views import hello, info, main_page, MenuView

urlpatterns = [
    path('', main_page),
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('info-page/', info),
    path('menu/', MenuView.as_view()),
]
