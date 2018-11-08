from django.forms import ModelForm
from .models import Logs

class AplicarForm(ModelForm):
    class Meta:
        model = Aplicar
        fields = '__all__'
