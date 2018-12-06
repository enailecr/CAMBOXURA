from dashboard.models import Dashboard
from datetime import datetime
import os, platform
import psutil

#class MyCronJob(CronJobBase):
def MyCronJob1():
    os.system("/bin/echo blablabla >> /tmp/teste") 
    swapp=psutil.swap_memory()
    #>>> swap[3] = porcentagem da SWAP usada
    #(total, used, free, percent, sin, sout)
    SWAPF = swapp[2]
    SWAPU = swapp[1]

    SWAP = swapp[3]
    disco = psutil.disk_usage('/')
    discoUsado = disco[1]
    discoLivre = disco[2]
    capacidadeDisco = disco[0]
    #>>> disco[3] = porcentagem do disco usado
    #(total, used, free, percent)

    CPU=int(psutil.cpu_percent())
    #porcentagem cpu
    
    mem = psutil.virtual_memory()
    RAM = mem[2]
    RAMU = mem[3]
    RAMF = mem[1]

    now=datetime.now()
    year= now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute

    dashboard = Dashboard(minute=minute,hour=hour,day=day,month=month,year=year,RAMU=RAMU,RAMF=RAMF,SWAP=SWAP, SWAPF=SWAPF,SWAPU=SWAPU,RAM=RAM,CPU=CPU,discoUsado=discoUsado,discoLivre=discoLivre,capacidadeDisco=capacidadeDisco)
    dashboard.save()
    #
    ##>>> mem[2] = porcentagem da memoria usada
    #(total, available, percent, used, free, active, inactive, buffers, cached, shared, slab)