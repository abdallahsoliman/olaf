# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dorm', '0003_auto_20151011_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='actuatortype',
            name='off_state_icon',
            field=models.CharField(default='moon', max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='actuatortype',
            name='on_state_icon',
            field=models.CharField(default='on', max_length=80),
            preserve_default=False,
        ),
    ]
