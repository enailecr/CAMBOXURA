from django.db import models
from destinos.models import Destino
from musicas.models import MusicaCategoria

class Anuncio(Destino):
    descricao = models.CharField(max_length=50, blank=False, null=False)
    gravacaoAn = models.ForeignKey('Gravacao', on_delete=models.CASCADE,)
    repeticao = models.IntegerField(blank=True, null=True)
    pula = models.BooleanField()
    retornaURA = models.BooleanField()
    canalNaoResp = models.BooleanField()
    destino = models.OneToOneField(
        Destino,
        on_delete=models.CASCADE,
        parent_link=True
    )

    def __str__(self):
        return self.descricao

class Gravacao(Destino):
    nome = models.CharField(max_length=30, blank=False, null=False)
    link = models.CharField(max_length=70, blank=False, null=False)
    musica = models.ForeignKey(MusicaCategoria, on_delete=models.CASCADE, null=True, blank=True)
