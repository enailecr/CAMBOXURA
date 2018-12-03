from django.db import models

class Dashboard(models.Model):
    CPU = models.FloatField()
    RAM = models.FloatField()
    SWAP = models.FloatField()
    #tempoFuncinamento = models.DateTimeField()
    discoUsado = models.FloatField()
    discoLivre = models.FloatField()
    #capacidadeDisco = models.IntegerField()
    #servicoTel = models.BooleanField()
    # servicoMsgInst = models.BooleanField()
    # servicoFax = models.BooleanField()
    # servicoEmail = models.BooleanField()
    # servicoBD = models.BooleanField()
    # servicoElastix = models.BooleanField()
