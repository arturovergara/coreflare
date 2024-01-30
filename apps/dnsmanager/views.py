# Django Imports
from django.views.generic import ListView, TemplateView

from .models import Website


class TestView(TemplateView):
    template_name = "dnsmanager/example.html"


class WebsiteListView(ListView):
    model = Website
