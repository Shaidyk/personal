from django.views.generic import TemplateView
from django.shortcuts import render
import datetime


class InfoView(TemplateView):
    template_name = "info.html"

    def get(self, request, *args, **kwargs):
        context = {
            "info_times": datetime.datetime.now().strftime("%d %b %Y, %H:%M:%S")
        }
        return render(request, self.template_name, context)
