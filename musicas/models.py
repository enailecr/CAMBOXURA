from django.db import models

class Musica(models.Model):
    nome = models.CharField(max_length=30, null=False, blank=False)

class Streaming(Musica):
    aplicacao = models.CharField(max_length=255, null=False, blank=False)
    formato = models.CharField(max_length=30, null=True, blank=True)

class MusicaCategoria(Musica):
    execRandom = models.BooleanField()
    volume = models.CharField(max_length=5)
