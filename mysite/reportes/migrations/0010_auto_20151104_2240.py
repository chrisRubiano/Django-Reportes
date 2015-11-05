# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0009_auto_20151104_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calibracion',
            name='costo',
            field=models.DecimalField(verbose_name=b'Costo (MXN)', max_digits=7, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='reparacion',
            name='costo',
            field=models.DecimalField(verbose_name=b'Costo (MXN)', max_digits=7, decimal_places=2),
        ),
    ]
