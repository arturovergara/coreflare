# Django Imports
from django.contrib import admin

from .models import Record, Website


class RecordInline(admin.TabularInline):
    model = Record
    extra = 1


@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ("domain", "is_active")
    inlines = (RecordInline,)
