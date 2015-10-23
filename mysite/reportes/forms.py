from django import forms
from .models import Reparacion, Calibracion
from django.contrib.admin.widgets import AdminDateWidget

class ReparacionForm(forms.ModelForm):

    class Meta:
        model = Reparacion 
        fields = ('fecha', 'numeroSerie', 'nombreTecnico', 'nombreEncargado', 'observaciones', 'costo')

class CalibracionForm(forms.ModelForm):

    class Meta:
        model = Calibracion
        fields = ('fecha', 'sigCalibracion', 'numeroSerie', 'nombreTecnico', 'nombreEncargado', 'observaciones', 'costo')