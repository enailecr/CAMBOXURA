from django.forms import ModelForm
from .models import NumeroEntrada

class NumeroEntradaForm(ModelForm):
    class Meta:
        model = NumeroEntrada
        fields = ('numero', 'origem', 'atendido', 'gravaChamada', 'destino')
        labels = {
            'numero': ('Número'),
            'gravaChamada': ('Grava chamada'),
        }
