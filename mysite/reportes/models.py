from django.db import models
from django.utils import timezone

def six_months_from_now():
    return timezone.now() + timezone.timedelta(days=180)

tecnicos = (
        ('Cristian Samaniego', 'Cristian Samaniego'),
        ('Esteban Miranda', 'Esteban Miranda'),
        ('Martin Ruiz', 'Martin Ruiz'),
        ('Dalia Arvizu','Dalia Arvizu'),
    )

#Modelo para guardar los reportes de reparacion
class Reparacion(models.Model):
	fecha = models.DateField('Fecha', default=timezone.now)
	cliente = models.CharField('Cliente', max_length=64, null=True)
	numeroSerie = models.CharField('Numero de Serie', max_length=36)
	nombreTecnico = models.CharField('Tecnico responsable', max_length=80, choices=tecnicos, blank=False, default=tecnicos)
	nombreEncargado = models.CharField('Encargado del area', max_length=80)
	observaciones = models.TextField('observaciones', blank=True, null=True)
	costo = models.DecimalField('Costo (MXN)', max_digits=8, decimal_places=2)

	class Meta:
		verbose_name = "Reparacion"
		verbose_name_plural = "Reparaciones"

	def __str__(self):
		return str(self.fecha)
		pass
    
#Modelo para guardar los reportes de calibracion
class Calibracion(models.Model):
	fecha = models.DateField('Fecha', default=timezone.now)
	cliente = models.CharField('Cliente', max_length=50, null=True)
	sigCalibracion = models.DateField('Siguiente Calibracion', default=six_months_from_now)
	numeroSerie = models.CharField('Numero de Serie', max_length=36)
	nombreTecnico = models.CharField('Tecnico responsable', max_length=80,choices=tecnicos, blank=False, default=tecnicos)
	nombreEncargado = models.CharField('Encargado del area', max_length=80)
	observaciones = models.TextField('Observaciones', blank=True, null=True)
	costo = models.DecimalField('Costo (MXN)', max_digits=8, decimal_places=2)

	class Meta:
		verbose_name = "Calibracion"
		verbose_name_plural = "Calibraciones"

	def __str__(self):
		return str(self.fecha)
		pass
