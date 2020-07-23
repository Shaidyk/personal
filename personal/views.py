from django.http import HttpResponse
import datetime


def hello(request):
    return HttpResponse("""
        <html>
            <body>
                <p style="color: red"> Hello Django!!! </p>
            </body>
        </html>
        """)


def info(request):
    return HttpResponse(
        f"""
        <html>
            <body style="background-color: gray">
                <h1 style="color: blue"> Now is {datetime.datetime.now()}</h1>
            </body>
        </html>
        """)


def main_page(request):
    return HttpResponse(
        f"""
            <html>
                <body style="background-color: green">
                    <b>
                    <div>
                        <a style="color: yellow" href=/admin/> Admin </a>  
                    </div>
                    <div>
                        <a style="color: yellow" href=/info-page/> Info-page </a>
                    </div>
                    <div>
                        <a style="color: yellow" href=/hello/> Hello </a>
                    </div>
                </body>
            </html>
            """)
