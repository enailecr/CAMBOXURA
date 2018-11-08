from django.db import models
from destinos.models import Destino

class NumeroEntrada(Destino):
    numero = models.IntegerField()
    origem = models.IntegerField()
    atendido = models.BooleanField()
    gravaChamada = models.BooleanField()
    destino = models.OneToOneField(
        Destino,
        on_delete=models.CASCADE,
        parent_link=True,
        related_name= 'destinoNumero'
    )

    def __str__(self):
        return self.numero
