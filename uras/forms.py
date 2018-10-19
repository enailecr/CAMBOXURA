from django.forms import ModelForm
from .models import ura

class ContatoForm(ModelForm):
    class Meta:
        model = ura
        fields = '__all__'