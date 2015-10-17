# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0002_auto_20151017_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calibracion',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now, verbose_name=b'Fecha'),
        ),
    ]
