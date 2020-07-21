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
            <body style="background-color: green">
                <h1 style="color: blue"> {datetime.datetime.today()}</h1>
            </body>
        </html>
        """)
