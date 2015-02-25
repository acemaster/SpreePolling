# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spreeevent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='alias',
            field=models.CharField(default='allure', max_length=300),
            preserve_default=False,
        ),
    ]
