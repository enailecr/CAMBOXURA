from django.forms import ModelForm
from .models import Fila

class FilaForm(ModelForm):
    class Meta:
        model = Fila
        fields = '__all__'