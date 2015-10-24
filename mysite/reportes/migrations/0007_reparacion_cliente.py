# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0006_calibracion_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='reparacion',
            name='cliente',
            field=models.CharField(max_length=64, null=True, verbose_name=b'Cliente'),
        ),
    ]
