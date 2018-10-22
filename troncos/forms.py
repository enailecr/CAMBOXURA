from django.forms import ModelForm
from .models import Tronco,TroncoSIP,TroncoIAX,TroncoCustomizado

class TroncoForm(ModelForm):
    class Meta:
        model = Tronco
        fields = '__all__'

class TroncoSIPForm(ModelForm):
    class Meta:
        model = TroncoSIP
        fields = '__all__'

class TroncoIAXForm(ModelForm):
    class Meta:
        model = TroncoIAX
        fields = '__all__'

class TroncoCustomizadoForm(ModelForm):
    class Meta:
        model = TroncoCustomizado
        fields = '__all__'