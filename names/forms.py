from django import forms
from .models import Iftar

class IftarForm(forms.ModelForm):
    class Meta:
        model = Iftar
        fields = ['person_name', 'iftar_name']