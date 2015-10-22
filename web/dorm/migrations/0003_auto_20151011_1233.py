# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dorm', '0002_auto_20151011_0317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actuator',
            name='name',
            field=models.CharField(unique=True, max_length=255),
        ),
    ]
