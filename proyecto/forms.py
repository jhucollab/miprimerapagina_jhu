from django import forms
from .models import Energia, Particula
#formulario energia particula
class EnergiaForm(forms.ModelForm):
    class Meta:
        model = Energia
        fields = ["tipo", "formula", "imagen"]
class ParticulaForm(forms.ModelForm):
    class Meta:
        model = Particula
        fields = ["carga_electrica", "nombre"]