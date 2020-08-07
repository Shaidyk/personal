from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render
import datetime
from .models import Category, MenuItem


class MenuView(TemplateView):
    template_name = "menu.html"

    # def get(self, request, *args, **kwargs):
    #     context = {
    #         'menu_items': MenuItem.objects.all()
    #     }
    #     return render(request, self.template_name, context)

    def get(self, request, *args, **kwargs):
        # queryset = MenuItem.objects.annotate(category=Category('name'))

        queryset = MenuItem.objects.all()

        filter_name = request.GET.get('filter')
        # if True:
        queryset = queryset.filter(category__name=filter_name)
        # queryset = queryset.order_by('category')

        context = {
            'menu_items': queryset
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


class InfoView(TemplateView):
    template_name = "info.html"

    def get(self, request, *args, **kwargs):
        context = {
            "info_times": datetime.datetime.now().strftime("%d %b %Y, %H:%M:%S")
        }
        return render(request, self.template_name, context)


def main_page(request):
    return render(request, "main.html")
