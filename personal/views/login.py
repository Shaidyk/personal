from django.shortcuts import render
from django.http import HttpResponseRedirect

from rest_framework.decorators import api_view, permission_classes


def authorization(request):
    return render(request, "login.html")


# @api_view(['GET'])
# @permission_classes([CanConfirmOrder & CanCompleteOrder])
def LoginView(request, format=None):
    return HttpResponseRedirect('/')


def login(request):
    return render(request, "main.html")
