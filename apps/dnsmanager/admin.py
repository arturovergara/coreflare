# Django Imports
from django.contrib import admin

from .models import Record, Website

admin.site.register(Website)
admin.site.register(Record)
