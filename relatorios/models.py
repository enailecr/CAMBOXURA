from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings

upload_storage = FileSystemStorage(location=settings.MEDIA2_ROOT, base_url=settings.MEDIA2_URL)

class Canal(models.Model):
    nome = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'Canal'

class Regex(models.Model):
    canal = models.ForeignKey(Canal, on_delete=models.CASCADE)
    expressao = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'Regex'

class Cdr(models.Model):
    calldate = models.DateTimeField(verbose_name='Data',)
    clid = models.CharField(max_length=80)
    src = models.CharField(verbose_name='Origem',max_length=80)
    dst = models.CharField(verbose_name='Destino',max_length=80)
    dcontext = models.CharField(max_length=80)
    channel = models.CharField(verbose_name='Canal Origem',max_length=80)
    dstchannel = models.CharField(verbose_name='Canal Destino',max_length=80)
    lastapp = models.CharField(max_length=80)
    lastdata = models.CharField(max_length=80)
    duration = models.IntegerField(verbose_name='Duração',)
    billsec = models.IntegerField()
    disposition = models.CharField(verbose_name='Status',max_length=45)
    amaflags = models.IntegerField()
    accountcode = models.CharField(verbose_name='Account Code',max_length=20)
    uniqueid = models.CharField(max_length=32, primary_key=True)
    userfield = models.CharField(max_length=255)
    recordingfile = models.FileField(storage=upload_storage, null=True, blank=True)
    cnum = models.CharField(max_length=40)
    cnam = models.CharField(max_length=40)
    outbound_cnum = models.CharField(max_length=40)
    outbound_cnam = models.CharField(max_length=40)
    dst_cnam = models.CharField(max_length=40)
    did = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cdr'

class Variaveis(models.Model):
    uniqueid = models.CharField(max_length=32)
    variavel = models.CharField(max_length=255, blank=True, null=True)
    valor = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'variaveis'
