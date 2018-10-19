from django.forms import ModelForm
from .models import URA

class UraForm(ModelForm):
    class Meta:
        model = URA
        fields = '__all__'