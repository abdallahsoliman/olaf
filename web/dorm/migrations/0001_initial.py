# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actuator',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('state', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ActuatorType',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('command_on', models.CharField(max_length=255)),
                ('command_off', models.CharField(max_length=255)),
                ('on_state_name', models.CharField(max_length=50)),
                ('off_state_name', models.CharField(max_length=50)),
                ('on_state_icon', models.CharField(max_length=80)),
                ('off_state_icon', models.CharField(max_length=80)),
            ],
        ),
        migrations.AddField(
            model_name='actuator',
            name='type',
            field=models.ForeignKey(to='dorm.ActuatorType'),
        ),
    ]
