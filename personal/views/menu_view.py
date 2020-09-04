from django.views.generic import TemplateView
from django.shortcuts import render

from ..models import MenuItem, Category


class MenuView(TemplateView):
    template_name = "menu.html"

    def get(self, request, *args, **kwargs):
        context = {"menu_items": []}

        queryset = MenuItem.objects.all()
        categories = Category.objects.all()

        for category in categories:
            items = queryset.filter(category=category).order_by('price')
            items = list(items)
            if items != []:
                result = {
                    'name': category,
                    'items': items
                }
                context['menu_items'].append(result)

        return render(request, self.template_name, context)