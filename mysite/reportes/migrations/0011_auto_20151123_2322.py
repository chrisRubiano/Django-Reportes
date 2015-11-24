# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0010_auto_20151104_2240'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='calibracion',
            options={'verbose_name': 'Calibracion', 'verbose_name_plural': 'Calibraciones'},
        ),
        migrations.AlterModelOptions(
            name='reparacion',
            options={'verbose_name': 'Reparacion', 'verbose_name_plural': 'Reparaciones'},
        ),
    ]
