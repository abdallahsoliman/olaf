# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dorm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actuatortype',
            name='name',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
