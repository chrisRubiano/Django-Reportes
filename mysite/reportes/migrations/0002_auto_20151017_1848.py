# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calibracion',
            name='sigCalibracion',
            field=models.DateField(verbose_name=b'Siguiente Calibracion'),
        ),
        migrations.AlterField(
            model_name='reparacion',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now, verbose_name=b'Fecha'),
        ),
    ]
