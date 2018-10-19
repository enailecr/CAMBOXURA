from django.forms import ModelForm
from .models import CondicaoTempo

class CondicaoTempoForm(ModelForm):
    class Meta:
        model = CondicaoTempo
        fields = '__all__'