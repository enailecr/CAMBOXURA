from django.db import models
from destinos.models import Destino
from musicas.models import MusicaCategoria

class Anuncio(Destino):
    descricao = models.CharField(max_length=50, blank=False, null=False)
    #coloquei como null= true
    gravacaoAn = models.ForeignKey('Gravacao', on_delete=models.CASCADE,null=True)
    repeticao = models.CharField(max_length=1,blank=True, null=True)
    pula = models.BooleanField()
    retornaURA = models.BooleanField()
    canalNaoResp = models.BooleanField()
    destino = models.IntegerField(null=True, blank=True)
    destinoTipo = models.CharField(max_length=1,blank=True, null=True)

    def __str__(self):
        return self.descricao

class Gravacao(Destino):
    nome = models.CharField(max_length=30, blank=False, null=False)
    link = models.CharField(max_length=255, blank=False, null=False)
    musica = models.ForeignKey(MusicaCategoria, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome
