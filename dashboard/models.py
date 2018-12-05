from django.db import models

class Dashboard(models.Model):
    CPU = models.IntegerField()
    RAM = models.FloatField()
    RAMU = models.BigIntegerField()
    RAMF = models.BigIntegerField()
    SWAP = models.FloatField()
    SWAPF = models.BigIntegerField()
    SWAPU = models.BigIntegerField()
    #tempoFuncinamento = models.DateTimeField()
    discoUsado = models.BigIntegerField()
    discoLivre = models.BigIntegerField()
    capacidadeDisco = models.BigIntegerField()
