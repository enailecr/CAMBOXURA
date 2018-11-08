from django.forms import ModelForm
from .models import Relatorios

class Relatorios(ModelForm):
    class Meta:
        model = Relatorios
        fields = '__all__'
