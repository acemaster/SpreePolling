# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spreeevent', '0002_events_alias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='name',
            field=models.CharField(max_length=128),
            preserve_default=True,
        ),
    ]
