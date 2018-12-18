from dashboard.models import Dashboard
from datetime import datetime
import os, platform
import psutil
from datetime import timedelta

#class MyCronJob(CronJobBase):
def MyCronJob1():
    os.system("/bin/echo blablabla >> /tmp/teste") 
    swapp=psutil.swap_memory()
    #>>> swap[3] = porcentagem da SWAP usada
    #(total, used, free, percent, sin, sout)
    SWAPF = swapp[2]
    SWAPU = swapp[1]

    SWAP = swapp[3]
    discot = psutil.disk_usage('/')
    discoUsado = discot[1]
    discoLivre = discot[2]
    capacidadeDisco = discot[0]
    disco=discot[3]
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
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
        uptime_string = str(timedelta(seconds = uptime_seconds))
    uptime_string= uptime_string[:-7]
    tempof=uptime_string
    dashboard = Dashboard(tempof=tempof,disco=disco,minute=minute,hour=hour,day=day,month=month,year=year,RAMU=RAMU,RAMF=RAMF,SWAP=SWAP, SWAPF=SWAPF,SWAPU=SWAPU,RAM=RAM,CPU=CPU,discoUsado=discoUsado,discoLivre=discoLivre,capacidadeDisco=capacidadeDisco)
    dashboard.save()
    #
    ##>>> mem[2] = porcentagem da memoria usada
    #(total, available, percent, used, free, active, inactive, buffers, cached, shared, slab)