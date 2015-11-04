# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import reportes.models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0007_reparacion_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calibracion',
            name='sigCalibracion',
            field=models.DateField(default=reportes.models.six_months_from_now, verbose_name=b'Siguiente Calibracion'),
        ),
    ]
