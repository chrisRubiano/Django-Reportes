from django.db import models
from django.utils import timezone

#Modelo para guardar los reportes de reparacion
class Reparacion(models.Model):
	fecha = models.DateField('Fecha', default=timezone.now)
	numeroSerie = models.CharField('Numero de Serie', max_length=36)
	nombreTecnico = models.CharField('Tecnico responsable', max_length=80)
	nombreEncargado = models.CharField('Encargado del area', max_length=80)
	observaciones = models.TextField('observaciones', blank=True, null=True)
	costo = models.DecimalField('Costo (MXN)', max_digits=5, decimal_places=2)

	def __str__(self):
		return str(self.fecha)
		pass
    
#Modelo para guardar los reportes de calibracion
class Calibracion(models.Model):
	fecha = models.DateField('Fecha', default=timezone.now)
	sigCalibracion = models.DateField('Siguiente Calibracion', )
	numeroSerie = models.CharField('Numero de Serie', max_length=36)
	nombreTecnico = models.CharField('Tecnico responsable', max_length=80)
	nombreEncargado = models.CharField('Encargado del area', max_length=80)
	observaciones = models.TextField('Observaciones', blank=True, null=True)
	costo = models.DecimalField('Costo (MXN)', max_digits=5, decimal_places=2)

	def __str__(self):
		return str(self.fecha)
		pass
    