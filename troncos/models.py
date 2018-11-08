from django.db import models
from destinos.models import Destino

OPCOESCID_CHOICES = (
    ('1' , 'Permitir qualquer CID'),
    ('2' , 'Bloquear CIDs estrangeiros'),
    ('3' , 'Remover CNAM'),
    ('4' , 'Forçar tronco CID'),
)

class Tronco(Destino):
    nome = models.CharField(max_length=40, null=False, blank=False)
    callerIDSaida = models.CharField(max_length=30, null=True, blank=True)
    opcoesCID = models.CharField(max_length=1,choices = OPCOESCID_CHOICES)
    maxCanais = models.IntegerField(null=True, blank=True)
    opcoesDiskAsterisk = models.CharField(max_length=30, null=True, blank=True)
    contSeOcup = models.BooleanField()
    desabTronco = models.BooleanField()
    prefixChamSaida = models.IntegerField()
    def __str__(self):
        return self.nome

class TroncoSIP(Tronco):
    nomeTronco = models.CharField(max_length=40, null=True, blank=True)
    detalhesPEER = models.TextField(null=True, blank=True)
    contextoUsuario = models.CharField(max_length=40, null=True, blank=True)
    detalhesUsuario = models.TextField(null=True, blank=True)
    stringRegistro = models.TextField(null=True, blank=True)

class TroncoIAX(Tronco):
    nomeTronco = models.CharField(max_length=40, null=True, blank=True)
    detalhesPEER = models.TextField(null=True, blank=True)
    contextoUsuario = models.CharField(max_length=40, null=True, blank=True)
    detalhesUsuario = models.TextField(null=True, blank=True)
    stringRegistro = models.TextField(null=True, blank=True)

class TroncoCustomizado(Tronco):
    stringChamada = models.CharField(max_length=200, null=True, blank=True)

class RegraManipulaNum(models.Model):
    precedente = models.IntegerField()
    prefixo = models.IntegerField()
    padrao = models.IntegerField()
    tronco = models.ForeignKey(Tronco, on_delete=models.CASCADE,)
