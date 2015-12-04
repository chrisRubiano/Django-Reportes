# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0011_auto_20151123_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calibracion',
            name='costo',
            field=models.DecimalField(verbose_name=b'Costo (MXN)', max_digits=8, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='calibracion',
            name='nombreTecnico',
            field=models.CharField(default=((b'Cristian Samaniego', b'Cristian Samaniego'), (b'Esteban Miranda', b'Esteban Miranda'), (b'Martin Ruiz', b'Martin Ruiz'), (b'Dalia Arvizu', b'Dalia Arvizu')), max_length=80, verbose_name=b'Tecnico responsable', choices=[(b'Cristian Samaniego', b'Cristian Samaniego'), (b'Esteban Miranda', b'Esteban Miranda'), (b'Martin Ruiz', b'Martin Ruiz'), (b'Dalia Arvizu', b'Dalia Arvizu')]),
        ),
        migrations.AlterField(
            model_name='reparacion',
            name='costo',
            field=models.DecimalField(verbose_name=b'Costo (MXN)', max_digits=8, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='reparacion',
            name='nombreTecnico',
            field=models.CharField(default=((b'Cristian Samaniego', b'Cristian Samaniego'), (b'Esteban Miranda', b'Esteban Miranda'), (b'Martin Ruiz', b'Martin Ruiz'), (b'Dalia Arvizu', b'Dalia Arvizu')), max_length=80, verbose_name=b'Tecnico responsable', choices=[(b'Cristian Samaniego', b'Cristian Samaniego'), (b'Esteban Miranda', b'Esteban Miranda'), (b'Martin Ruiz', b'Martin Ruiz'), (b'Dalia Arvizu', b'Dalia Arvizu')]),
        ),
    ]
