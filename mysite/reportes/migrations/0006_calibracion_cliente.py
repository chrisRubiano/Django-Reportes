# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0005_auto_20151021_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='calibracion',
            name='cliente',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Cliente'),
        ),
    ]
