# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actuator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('state', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ActuatorType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('command_on', models.CharField(max_length=255)),
                ('command_off', models.CharField(max_length=255)),
                ('on_state_name', models.CharField(max_length=50)),
                ('off_state_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='actuator',
            name='type',
            field=models.ForeignKey(to='dorm.ActuatorType'),
        ),
    ]
