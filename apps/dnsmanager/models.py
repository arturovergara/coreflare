# Django Imports
from django.db import models


class Website(models.Model):
    domain = models.CharField(max_length=253, unique=True)
    is_active = models.BooleanField(default=True)
    is_starred = models.BooleanField(default=False)


class Record(models.Model):
    class RecordTypes(models.IntegerChoices):
        A = 0, "A"
        AAAA = 1, "AAAA"
        CNAME = 2, "CNAME"
        MX = 3, "MX"
        NS = 4, "NS"
        PTR = 5, "PTR"
        TXT = 6, "TXT"

    record_type = models.PositiveSmallIntegerField(choices=RecordTypes.choices)
    name = models.CharField(max_length=63)
    value = models.CharField(max_length=255)
    observation = models.TextField(null=True, blank=True)
    website = models.ForeignKey(
        "Website", on_delete=models.CASCADE, related_name="records"
    )
