from dashboard.models import Dashboard
import os, platform
import psutil

#class MyCronJob(CronJobBase):
def MyCronJob():
    ##os.system("echo blablabla >> /tmp/teste");
    dashboard = Dashboard.objects.all()

    swap=psutil.swap_memory()
    #>>> swap[3] = porcentagem da SWAP usada
    #(total, used, free, percent, sin, sout)

    dashboard.SWAP = swap[3]
    disco = psutil.disk_usage('/')
    dashboard.discoUsado = disco[3]
    dashboard.discoLivre = 100 - disco[3]
    dashboard.capacidadeDisco = disco[0]
    #>>> disco[3] = porcentagem do disco usado
    #(total, used, free, percent)

    cpu=psutil.cpu_percent()
    dashboard.CPU = cpu
    #porcentagem cpu
    
    mem = psutil.virtual_memory()
    dashboard.RAM = mem[2]
    ##>>> mem[2] = porcentagem da memoria usada
    #(total, available, percent, used, free, active, inactive, buffers, cached, shared, slab)