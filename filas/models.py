from django.db import models
from destinos.models import Destino
from anuncios.models import Anuncio
from numeros.models import NumeroEntrada
from uras.models import URA

RESTRICOESAGENTE_CHOICES = (
    ('1', 'Chamada como discada'),
    ('2', 'Sem Me-Siga ou Chamada para Frente'),
    ('3', 'Apenas extensões'),
)

ESTRATEGIACHAMADA_CHOICES = (
    ('1', 'ringall'),
    ('2', 'leastrecent'),
    ('3', 'fewestcalls'),
    ('4', 'random'),
    ('5', 'rrmemory'),
    ('6', 'rrordered'),
    ('7', 'linear'),
    ('8', 'wrandom'),
)

IGNORAAGENTOCUP_CHOICES = (
    ('1', 'Sim'),
    ('2', 'Não'),
    ('3', 'Sim + (chamadaemuso=não)'),
    ('4', 'Somente chamada em fila (chamadaemuso=não)'),
)

TIPOMUS_CHOICES = (
    ('1', 'Apenas MoH'),
    ('2', 'Agente tocando'),
    ('3', 'Apenas chamar'),
)

QUANDOANUNCIO_CHOICES = (
    ('1', 'Sempre'),
    ('2', 'Quando não há agentes livres'),
    ('3', 'Quando não há agentes prontos'),
)

QUANDOANUNCIO_CHOICES = (
    ('1', 'Sempre'),
    ('2', 'Quando não há agentes livres'),
    ('3', 'Quando não há agentes prontos'),
)
GRAVACAOCHAMADA_CHOICES = (
    ('1', 'Não'),
    ('2', 'wav49'),
    ('3', 'wav'),
    ('4', 'gsm'),
)

MODOGRAVACAO_CHOICES = (
    ('1', 'Incluir tempo de espera'),
    ('2', 'Após resposta'),
)

AJUSTEVOLUME_CHOICES = (
        ('1', 'Sem ajuste'),
        ('2', '-4'),
        ('3', '-3'),
        ('4', '-2'),
        ('5', '-1'),
        ('6', '+1'),
        ('7', '+2'),
        ('8', '+3'),
        ('9', '+4'),
)

MODOMAXESPERA_CHOICES = (
    ('1', 'Estrito'),
    ('2', 'Livre'),
)

PAUSAAUTOMATICA_CHOICES = (
    ('1', 'Não'),
    ('2', 'Sim ,apenas nessa fila'),
    ('3', 'Sim, em todas as filas'),
)

UNIRVAZIO_CHOICES = (
        ('1', 'Sim'),
        ('2', 'Não'),
        ('3', 'Estrito'),
        ('4', 'Extremamente estrito'),
        ('5', 'Livre'),
)

DEIXARVAZIO_CHOICES = (
    ('1', 'Não'),
    ('2', 'Sim'),
    ('3', 'Estrito'),
    ('4', 'Extremamente estrito'),
    ('5', 'Livre'),
)

ANUNCTEMPOESPERA_CHOICES = (
    ('1', 'Não'),
    ('2', 'Sim'),
    ('3', 'Uma vez'),
)

HABDESAB_CHOICES = (
    ('1', 'Habilitado'),
    ('2', 'Desabilitado'),
)

REPORESTATISTICAS_CHOICES = (
    ('1', 'Nunca'),
    ('2', 'De hora em hora'),
    ('3', 'Diariamente'),
    ('4', 'Semanalmente'),
    ('5', 'Mensalmente'),
    ('6', 'Anualmente'),
    ('6', 'Reiniciar'),
)

class Fila(Destino):
    nome = models.CharField(max_length=40, blank=False, null=False)
    senha = models.CharField(max_length=40, blank=False, null=False)
    dicasDisp = models.BooleanField()
    confirmCham = models.BooleanField()
    anuncConfirmCham = models.ForeignKey(Anuncio, on_delete=models.CASCADE, null = True, related_name='anuncConfirmChamFila')
    prefixCID = models.IntegerField()
    prefixTempoEspera = models.BooleanField()
    infoAlerta = models.CharField(max_length=70)
    restringAgentDin = models.BooleanField()
    restricAgente = models.CharField(max_length=1,choices = RESTRICOESAGENTE_CHOICES, blank=False, null=False)
    estratChamada = models.CharField(max_length=1,choices = ESTRATEGIACHAMADA_CHOICES, blank=False, null=False)
    preenchAuto = models.BooleanField()
    igAgentesOcup = models.CharField(max_length=1,choices = IGNORAAGENTOCUP_CHOICES, blank=False, null=False)
    pesoFila = models.IntegerField()
    #musEspera =
    tipoMus = models.CharField(max_length=1,choices = TIPOMUS_CHOICES, blank=False, null=False)
    anuncUniao = models.ForeignKey(Anuncio, on_delete=models.CASCADE, null = True, related_name='anuncUniaoFila')
    quandoAnun = models.CharField(max_length=1,choices = QUANDOANUNCIO_CHOICES, blank=False, null=False)
    gravacaoChamada = models.CharField(max_length=1,choices = GRAVACAOCHAMADA_CHOICES, blank=False, null=False)
    modoGravacao = models.CharField(max_length=1,choices = MODOGRAVACAO_CHOICES, blank=False, null=False)
    ajustVolumeChamada = models.CharField(max_length=1,choices = AJUSTEVOLUME_CHOICES, blank=False, null=False)
    ajustVolumeAgente = models.CharField(max_length=1,choices = AJUSTEVOLUME_CHOICES, blank=False, null=False)
    marcaChamOutroLug = models.BooleanField()
    maxTempoEspera = models.TimeField(null=True)
    modoMaxTempoEspera = models.CharField(max_length=1,choices = MODOMAXESPERA_CHOICES, blank=False, null=False)
    tempoLimAgent = models.TimeField(null=True)
    reinicioTempoLimAg = models.BooleanField()
    retentativa = models.TimeField(null=True, blank=True)
    tempoConclusao = models.TimeField(null=True, blank=True)
    atrasoMembro = models.TimeField(null=True, blank=True)
    anuncioAgente = models.ForeignKey(Anuncio, on_delete=models.CASCADE, null = True, related_name='anuncioAgenteFila')
    relatorioTemEsp = models.BooleanField()
    pausaAutom = models.CharField(max_length=1,choices = PAUSAAUTOMATICA_CHOICES, blank=False, null=False)
    pausaAutoOcup = models.BooleanField()
    pausaAutoIndispo = models.BooleanField()
    atrasoPausaAut = models.IntegerField()
    maxChamadores = models.IntegerField()
    unirVazio = models.CharField(max_length=1,choices = UNIRVAZIO_CHOICES, blank=False, null=False)
    deixarVazio = models.CharField(max_length=1,choices = DEIXARVAZIO_CHOICES, blank=False, null=False)
    limMembrosPenal = models.IntegerField()
    frequencia = models.TimeField(null=True, blank=True)
    posAnuncio = models.BooleanField()
    anuncTempoEsp = models.CharField(max_length=1,choices = ANUNCTEMPOESPERA_CHOICES, blank=False, null=False)
    menuSaidaURA = models.ForeignKey(URA, on_delete=models.CASCADE, null = True)
    frequenRepet = models.TimeField(null=True, blank=True)
    eventChamado = models.CharField(max_length=1,choices = HABDESAB_CHOICES, blank=False, null=False)
    eventStatusMem = models.CharField(max_length=1,choices = HABDESAB_CHOICES, blank=False, null=False)
    nivelServico = models.TimeField(null=False, blank=False)
    filtro = models.CharField(max_length=20, null=True, blank=True)
    destinoFalha = models.OneToOneField(
        Destino,
        on_delete=models.CASCADE,
        parent_link=True,
        related_name= 'destinoFalhaFila'
    )
    reporEstat = models.CharField(max_length=1,choices = REPORESTATISTICAS_CHOICES, blank=False, null=False)

class AgentesDinamicos(models.Model):
    fila = models.ForeignKey('Fila', on_delete=models.CASCADE)
    numero = models.ForeignKey(NumeroEntrada, on_delete=models.CASCADE)
    ordem =models.IntegerField()

class MembrosDinamicos(models.Model):
    fila = models.ForeignKey('Fila', on_delete=models.CASCADE)
    numero = models.ForeignKey(NumeroEntrada, on_delete=models.CASCADE)
    ordem =models.IntegerField()
