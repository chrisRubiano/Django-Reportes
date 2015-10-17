from django import forms
from .models import Reparacion, Calibracion

class ReparacionForm(forms.ModelForm):

    class Meta:
        model = Reparacion 
        fields = ('fecha', 'numeroSerie', 'nombreTecnico', 'nombreEncargado', 'observaciones', 'costo')