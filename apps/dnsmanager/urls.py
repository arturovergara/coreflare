# Django Imports
from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from .views import TestView, WebsiteCreateView, WebsiteDetailView, WebsiteListView

app_name = "dnsmanager"
urlpatterns = [
    path(
        "websites/<str:domain>/dns/records/",
        WebsiteDetailView.as_view(),
        name="website_detail",
    ),
    path("websites/add/", WebsiteCreateView.as_view(), name="website_create"),
    path("websites/", WebsiteListView.as_view(), name="website_list"),
    path("test/", TestView.as_view(), name="test"),
    path(
        "",
        RedirectView.as_view(url=reverse_lazy("dnsmanager:website_list")),
        name="home",
    ),
]
