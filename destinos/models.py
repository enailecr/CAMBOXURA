from django.db import models

TIPO_CHOICES = (
    ('1','Anúncio'),
    ('2','Gravação'),
    ('3','Número de entrada'),
    ('4','URA'),
    ('5','Fila'),
    ('6','Chamada em grupo'),
    ('7','Condições de tempo'),
    ('8','Tronco'),
)

class Destino(models.Model):
    class Meta:
        abstract = True

    tipo = models.CharField(max_length=1, blank=False, null=False, choices = TIPO_CHOICES)
