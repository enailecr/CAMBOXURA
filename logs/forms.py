from django.forms import ModelForm
from .models import Logs

class LogsForm(ModelForm):
    class Meta:
        model = Logs
        fields = '__all__'
