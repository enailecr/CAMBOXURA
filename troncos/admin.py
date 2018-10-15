from django.contrib import admin
from .models import Tronco, TroncoSIP, TroncoIAX, TroncoCustomizado, RegraManipulaNum

admin.site.register(Tronco)
admin.site.register(TroncoSIP)
admin.site.register(TroncoIAX)
admin.site.register(TroncoCustomizado)
admin.site.register(RegraManipulaNum)
