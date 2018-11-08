from django.db import models

class Logs():
    data = models.CharField(max_length=30, null=False, blank=False)