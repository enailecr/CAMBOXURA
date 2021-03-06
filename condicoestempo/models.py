from django.db import models
from destinos.models import Destino
import calendar

MONTH_CHOICES = [(str(i), calendar.month_name[i]) for i in range(1,13)]
SEMANA_CHOICES = [(str(i), calendar.day_name[i]) for i in range(1,7)]
DIAS_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
    ('13', '13'),
    ('14', '14'),
    ('15', '15'),
    ('16', '16'),
    ('17', '17'),
    ('18', '18'),
    ('19', '19'),
    ('20', '20'),
    ('21', '21'),
    ('22', '22'),
    ('23', '23'),
    ('24', '24'),
    ('25', '25'),
    ('26', '26'),
    ('27', '27'),
    ('28', '28'),
    ('29', '29'),
    ('30', '30'),
    ('31', '31'),
)

class CondicaoTempo(Destino):
    nome = models.CharField(max_length=30, null=False, blank=False)
    destinoCoincide =models.IntegerField(null=True, blank=True)
    destinoCoincideTipo = models.CharField(max_length=1,blank=True, null=True)
    destinoNaoCoincide =models.IntegerField(null=True, blank=True)
    destinoNaoCoincideTipo = models.CharField(max_length=1,blank=True, null=True)
    def __str__(self):
        return self.nome

class GrupoTempo(Destino):
    horaInicio = models.TimeField()
    horaFim = models.TimeField()
    diaSemanaInicio = models.CharField(max_length=13, choices=SEMANA_CHOICES)
    diaSemanaFim = models.CharField(max_length=13, choices=SEMANA_CHOICES)
    diaMesInicio = models.CharField(max_length=2, choices=DIAS_CHOICES)
    diaMesFim = models.CharField(max_length=2, choices=DIAS_CHOICES)
    mesIncio = models.CharField(max_length=9, choices=MONTH_CHOICES)
    mesFim = models.CharField(max_length=9, choices=MONTH_CHOICES)
    #null para teste
    condTempo = models.ForeignKey('CondicaoTempo', on_delete=models.CASCADE,null= True)
