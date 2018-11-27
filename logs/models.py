from django.db import models

class Log(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    log = models.CharField(max_length=255, null=False, blank=False)
