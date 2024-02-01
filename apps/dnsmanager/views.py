# Django Imports
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, TemplateView

from .forms import WebsiteForm
from .models import Website


class TestView(TemplateView):
    template_name = "dnsmanager/example.html"


class WebsiteListView(ListView):
    model = Website
    context_object_name = "websites"


class WebsiteCreateView(CreateView):
    model = Website
    form_class = WebsiteForm
    success_url = reverse_lazy("dnsmanager:website_list")
    success_message = "Website was created successfully!"


class WebsiteDetailView(DetailView):
    model = Website
    context_object_name = "website"
    slug_field = "domain"
    slug_url_kwarg = "domain"
