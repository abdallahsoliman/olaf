# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0006_auto_20150725_1436'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='phonenumber',
            unique_together=set([('contact', 'phone_number')]),
        ),
    ]
