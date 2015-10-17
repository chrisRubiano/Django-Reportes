# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calibracion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'Fecha')),
                ('sigCalibracion', models.DateTimeField(verbose_name=b'Siguiente Calibracion')),
                ('numeroSerie', models.CharField(max_length=36, verbose_name=b'Numero de Serie')),
                ('nombreTecnico', models.CharField(max_length=80, verbose_name=b'Tecnico responsable')),
                ('nombreEncargado', models.CharField(max_length=80, verbose_name=b'Encargado del area')),
                ('observaciones', models.TextField(null=True, verbose_name=b'Observaciones', blank=True)),
                ('costo', models.DecimalField(verbose_name=b'Costo', max_digits=5, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Reparacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'Fecha')),
                ('numeroSerie', models.CharField(max_length=36, verbose_name=b'Numero de Serie')),
                ('nombreTecnico', models.CharField(max_length=80, verbose_name=b'Tecnico responsable')),
                ('nombreEncargado', models.CharField(max_length=80, verbose_name=b'Encargado del area')),
                ('observaciones', models.TextField(null=True, verbose_name=b'observaciones', blank=True)),
                ('costo', models.DecimalField(verbose_name=b'Costo', max_digits=5, decimal_places=2)),
            ],
        ),
    ]
