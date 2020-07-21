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
            <body>
                <h2 style="color: blue"> {datetime.datetime.today()}</h2>
            </body>
        </html>
        """)
