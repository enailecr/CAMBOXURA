from django.forms import ModelForm
from .models import ChamadaEmGrupo

class ChamadaEmGrupoForm(ModelForm):
    class Meta:
        model = ChamadaEmGrupo
        fields = ('descricao', 'estrategia', 'tempoChamada', 'anuncioCG', 'musicaEspera', 'prefixCID', 'infoAlerta', 'igConfigCF', 'igAgentOcupado','atendeChamada', 'confirmaChamada', 'anuncioRemoto', 'anuncioTardio', 'modo', 'valorFixoCID', 'gravarChamadas', 'destino')
        labels = {
            'descricao': ('Descrição do grupo'),
            'estrategia': ('Estratégia de chamada'),
            'tempoChamada': ('Tempo Chamada(máx 300 seg)'),
            'anuncioCG': ('Anúncio'),
            'musicaEspera': ('Tocar música em espera?'),
            'prefixCID': ('Prefixo de nome CID'),
            'infoAlerta': ('Informação de alerta'),
            'igConfigCF': ('Ignorar configurações CF'),
            'igAgentOcupado': ('Ignorar agente ocupado'),
            'atendeChamada': ('Permitir atender chamada'),
            'confirmaChamada': ('Confirmar chamadas'),
            'anuncioRemoto': ('Anúncio remoto'),
            'gravaChamada': ('Gravar chamadas'),
            'anuncioTardio': ('Anúncio tardio'),
            'valorFixoCID': ('Valor fixo de CID'),
            'destino': ('Destino se não houver resposta'),
        }

# class ListaExtensaoForm(ModelForm):
#     class Meta:
