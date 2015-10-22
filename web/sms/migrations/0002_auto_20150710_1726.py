# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=160)),
                ('received_at', models.DateTimeField(auto_now_add=True)),
                ('sender', models.ForeignKey(to='sms.Contact')),
            ],
        ),
        migrations.RemoveField(
            model_name='sms',
            name='sender',
        ),
        migrations.DeleteModel(
            name='SMS',
        ),
    ]
