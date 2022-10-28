from django.views.generic import ListView

from apps.catalog.models import Category


class MenuView(ListView):
    model = Category
    template_name = 'menu.html'


# Create your views here.
