# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import swampdragon.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HeartRate',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            bases=(swampdragon.models.SelfPublishModel, models.Model),
        ),
    ]
