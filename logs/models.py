from django.db import models

class Logs(models.Model):
    data = models.CharField(max_length=30, null=False, blank=False)
    ata = models.CharField(max_length=30, null=False, blank=False)
