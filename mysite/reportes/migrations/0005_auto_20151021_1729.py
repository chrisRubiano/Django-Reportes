# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0004_auto_20151017_1850'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='calibracion',
            options={'verbose_name': 'Calibracion'},
        ),
        migrations.AlterModelOptions(
            name='reparacion',
            options={'verbose_name': 'Reparacion'},
        ),
    ]
