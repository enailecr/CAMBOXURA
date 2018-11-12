from django.db import models
from destinos.models import Destino
from anuncios.models import Anuncio
from numeros.models import NumeroEntrada
from musicas.models import Musica

ESTRATEGIA_CHOICES = (
    ('1','ringall'),
    ('2','ringall-prim'),
    ('3','hunt'),
    ('4','hunt-prim'),
    ('5','memoryhunt'),
    ('6','memoryhunt-prim'),
    ('7','firstavaible'),
    ('8','firstnotonphone'),
)

MODO_CHOICES = (
    ('1','Padrão'),
    ('2','Valor fixo de CID'),
    ('3','Valor fixo de CID de chamadas externas'),
    ('4','Usar número discado'),
    ('5','Forçar número discado'),
)

GRAVARCHAMADAS_CHOICES = (
    ('1','Sempre'),
    ('2','Sob demanda'),
    ('3','Nunca'),
)

class ChamadaEmGrupo(Destino):
    descricao = models.CharField(max_length=70, null=False, blank=False)
    estrategia = models.CharField(max_length=1,choices = ESTRATEGIA_CHOICES, null=False, blank=False)
    tempoChamada = models.IntegerField()
    anuncioCG = models.ForeignKey(Anuncio, on_delete=models.CASCADE,null=True,related_name='anuncioCG')
    musicaEspera = models.ForeignKey(Musica,null=True, on_delete=models.CASCADE)
    prefixCID = models.CharField(max_length=10)
    infoAlerta = models.CharField(max_length=70)
    igConfigCF = models.BooleanField()
    igAgentOcupado = models.BooleanField()
    atendeChamada = models.BooleanField()
    confirmaChamada = models.BooleanField(null=True,)
    anuncioRemoto =  models.ForeignKey(Anuncio,null=True, on_delete=models.CASCADE, related_name='anuncioRemotoCG')
    anuncioTardio =  models.ForeignKey(Anuncio,null=True, on_delete=models.CASCADE,related_name='anuncioTardioCG')
    modo = models.CharField(max_length=1,choices = MODO_CHOICES)
    valorFixoCID = models.CharField(max_length=30, null=True, blank=True)
    gravarChamadas = models.CharField(max_length=1,choices = GRAVARCHAMADAS_CHOICES, null=False, blank=False)
    destino = models.IntegerField(blank=True, null=True)
    destinoTipo = models.CharField(max_length=1,blank=True, null=True)

    def __str__(self):
        return self.descricao

class ListaExtensao(models.Model):
    chamada = models.ForeignKey('ChamadaEmGrupo', on_delete=models.CASCADE)
    numero = models.ForeignKey(NumeroEntrada, on_delete=models.CASCADE)
    ordem = models.IntegerField()
