# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0005_auto_20150725_1429'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='last_name',
        ),
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(default='Bill', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(to='sms.Contact'),
        ),
        migrations.AlterField(
            model_name='phonenumber',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be in the format: '+####', with 15 digits MAX.")]),
        ),
    ]
