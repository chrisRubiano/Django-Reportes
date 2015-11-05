# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0008_auto_20151104_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calibracion',
            name='nombreTecnico',
            field=models.CharField(default=((b'Cristian Samaniego', b'Cristian Samaniego'), (b'Alan Sanchez', b'Alan Sanchez'), (b'Ivan Coronel', b'Ivan Coronel')), max_length=80, verbose_name=b'Tecnico responsable', choices=[(b'Cristian Samaniego', b'Cristian Samaniego'), (b'Alan Sanchez', b'Alan Sanchez'), (b'Ivan Coronel', b'Ivan Coronel')]),
        ),
        migrations.AlterField(
            model_name='reparacion',
            name='nombreTecnico',
            field=models.CharField(default=((b'Cristian Samaniego', b'Cristian Samaniego'), (b'Alan Sanchez', b'Alan Sanchez'), (b'Ivan Coronel', b'Ivan Coronel')), max_length=80, verbose_name=b'Tecnico responsable', choices=[(b'Cristian Samaniego', b'Cristian Samaniego'), (b'Alan Sanchez', b'Alan Sanchez'), (b'Ivan Coronel', b'Ivan Coronel')]),
        ),
    ]
