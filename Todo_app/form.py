from .models import todo
from django.forms import ModelForm,TextInput

class todoform(ModelForm):
    class Meta:
        model = todo
        fields = '__all__'
       