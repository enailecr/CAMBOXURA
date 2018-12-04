from django.db import models

class Dashboard(models.Model):
    CPU = models.FloatField()
    RAM = models.FloatField()
    RAMU = models.BigIntegerField()
    RAMF = models.BigIntegerField()
    SWAP = models.FloatField()
    SWAPF = models.BigIntegerField()
    SWAPU = models.BigIntegerField()
    #tempoFuncinamento = models.DateTimeField()
    discoUsado = models.FloatField()
    discoLivre = models.FloatField()
    capacidadeDisco = models.BigIntegerField()
