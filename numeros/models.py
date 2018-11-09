from django.db import models
from destinos.models import Destino

class NumeroEntrada(Destino):
    numero = models.IntegerField()
    origem = models.IntegerField()
    atendido = models.BooleanField()
    gravaChamada = models.BooleanField()
    destino =models.IntegerField()
    destinoTipo = models.CharField(max_length=1,blank=True, null=True)

    def __str__(self):
        return self.numero
