# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0007_auto_20150725_1510'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phonenumber',
            old_name='phone_number',
            new_name='number',
        ),
        migrations.AlterUniqueTogether(
            name='phonenumber',
            unique_together=set([('contact', 'number')]),
        ),
    ]
