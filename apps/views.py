import datetime

from django.http import HttpResponse
from django.views.generic import TemplateView, View

from apps.catalog.models import Category


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context


class AboutView(TemplateView):
    template_name = 'about.html'
    extra_context = {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.date.today()
        return context


class SimpleView(View):
    def get(self, request, *args, year=None, **kwargs):
        print(args)
        print(year)
        return HttpResponse()

    def post(self, request, *args, **kwargs):
        return HttpResponse()
