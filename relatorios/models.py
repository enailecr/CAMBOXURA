from django.db import models


class Relatorios(models.Model):
    data = models.BooleanField()
    retornaURA = models.BooleanField()
    canalNaoResp = models.BooleanField()
