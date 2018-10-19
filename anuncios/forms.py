from django.forms import ModelForm
from .models import Anuncio

class AnuncioForm(ModelForm):
    class Meta:
        model = Anuncio
        fields = '__all__'