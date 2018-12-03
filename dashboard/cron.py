from dashboard.models import Dashboard
import os, platform
import psutil

#class MyCronJob(CronJobBase):
def MyCronJob1():
    os.system("/bin/echo blablabla >> /tmp/teste") 
    swapp=psutil.swap_memory()
    #>>> swap[3] = porcentagem da SWAP usada
    #(total, used, free, percent, sin, sout)

    SWAP = swapp[3]
    disco = psutil.disk_usage('/')
    discoUsado = disco[3]
    discoLivre = 100 - disco[3]
    #capacidadeDisco = disco[0]
    #>>> disco[3] = porcentagem do disco usado
    #(total, used, free, percent)

    CPU=psutil.cpu_percent()
    #porcentagem cpu
    
    mem = psutil.virtual_memory()
    RAM = mem[2]
    dashboard = Dashboard(SWAP=SWAP,RAM=RAM,CPU=CPU,discoUsado=discoUsado,discoLivre=discoLivre)
    dashboard.save()
    #,capacidadeDisco=capacidadeDisco
    ##>>> mem[2] = porcentagem da memoria usada
    #(total, available, percent, used, free, active, inactive, buffers, cached, shared, slab)