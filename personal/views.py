from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render
import datetime
from .models import Category, Order


class MenuView(TemplateView):
    template_name = "menu.html"

    def get(self, request, *args, **kwargs):
        context = {
            'menu_items': Category.objects.all()
        }
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


def info(request):
    return HttpResponse(
        f"""
        <html>
            <header></header>
            <body style="background-color: gray">
                <h1 style="color: blue"> Now is {datetime.datetime.now()}</h1>
                <a style="color: yellow" href=/> "Main-page" </a>
            </body>
        </html>
        """)



def main_page(request):
    return render(request, "main.html")
