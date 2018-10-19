from django.forms import ModelForm
from .models import Streaming, MusicaCategoria

class StreamingForm(ModelForm):
    class Meta:
        model = Streaming
        fields = '__all__'

class MusicaForm(ModelForm):
    class Meta:
        model = MusicaCategoria
        fields = '__all__'