from django.db import models
from destinos.models import Destino
from anuncios.models import Anuncio, Gravacao

DISCARDIRETO_CHOICES = (
    ('1', 'Desabilitado'),
    ('2', 'Ramais'),
)


class URA(Destino):
    nome = models.CharField(max_length=40, blank=False, null=False)
    descricao = models.CharField(max_length=10, blank=False, null=False)
    anuncioUra = models.ForeignKey(Anuncio, on_delete=models.SET_NULL, null=True, blank=True)
    discarDireto = models.CharField(max_length=1,choices = DISCARDIRETO_CHOICES)
    timeout = models.IntegerField()
    tentativasInvalidas = models.IntegerField()
    gravRepetInvalid = models.ForeignKey(Gravacao, on_delete=models.SET_NULL, null=True, blank=True)
    anexAnuncInvalid = models.BooleanField()
    returnInvalid = models.BooleanField()
    gravInvalid = models.ForeignKey(Gravacao, on_delete=models.SET_NULL, null=True, blank=True,related_name='gravInvalidURA')
    destinoInvalid = models.OneToOneField(
        Destino,
        on_delete=models.CASCADE,
        parent_link=True,
        related_name= 'destinoInvalidURA'
    )
    retentativasTimeout = models.IntegerField()
    gravRetentTimeout = models.ForeignKey(Gravacao, on_delete=models.SET_NULL, null=True, blank=True,related_name='gravRepetInvalidURA')
    anexAnuncTimeout = models.BooleanField()
    retornarTimeout = models.BooleanField()
    gravTimeout = models.ForeignKey(Gravacao, on_delete=models.SET_NULL, null=True, blank=True,related_name='gravTimeoutURA')
    destinoTimeout = models.OneToOneField(
        Destino,
        on_delete=models.CASCADE,
        parent_link=True,
        related_name='destinoTimeoutURA'
    )
    returnURACaixaPostal = models.BooleanField()

class OpcaoURA(models.Model):
    ura = models.ForeignKey('URA', on_delete=models.CASCADE,)
    destino = models.OneToOneField(
        Destino,
        on_delete=models.CASCADE,
        parent_link=True
    )
    retornar = models.BooleanField()
