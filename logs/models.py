from django.db import models

class Log(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    log = models.CharField(max_length=255, null=False, blank=False)

class LogCambox:
    def __init__(self, data, tipo, processo, chamada ,log):
        self.data = data
        self.tipo = tipo
        self.processo = processo
        self.chamada = chamada
        self.log = log
