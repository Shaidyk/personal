from django.http import HttpResponse
from django.views.generic import TemplateView
import datetime


class Menu(TemplateView):
    template_name = "menu.html"


def hello(request):
    return HttpResponse("""
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
    return HttpResponse(
        """
            <html>
                <body style="background-color: green">
                    <b>
                    <div>
                        <a style="color: yellow" href="/admin/"> Admin </a>  
                    </div>
                    <div>
                        <a style="color: yellow" href="/info-page/"> Info-page </a>
                    </div>
                    <div>
                        <a style="color: yellow" href="/hello/"> Hello </a>
                    </div>
                    <div>
                        <a style="color: yellow" href="/menu/"> Menu </a>
                    </div>
                </body>
            </html>
        """)
