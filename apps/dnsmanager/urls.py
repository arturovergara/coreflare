# Django Imports
from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from .views import TestView

app_name = "console"
urlpatterns = [
    path("test/", TestView.as_view(), name="test"),
    path(
        "",
        RedirectView.as_view(url=reverse_lazy("console:test")),
        name="home",
    ),
]
