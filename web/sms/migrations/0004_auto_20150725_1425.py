# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0003_auto_20150715_1647'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be in the format: '+####', with 15 digits MAX.")])),
            ],
        ),
        migrations.RemoveField(
            model_name='contact',
            name='phone_number',
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(to='sms.PhoneNumber'),
        ),
        migrations.AddField(
            model_name='phonenumber',
            name='contact',
            field=models.ForeignKey(to='sms.Contact'),
        ),
    ]
