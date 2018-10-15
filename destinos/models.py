from django.db import models

class Destino(models.Model):
    tipo = models.CharField(max_length=30, blank=False, null=False)
