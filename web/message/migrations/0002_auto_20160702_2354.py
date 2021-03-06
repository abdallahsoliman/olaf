# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-03 03:54
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonenumber',
            name='number',
            field=models.CharField(blank=True, max_length=20, validators=[django.core.validators.RegexValidator(message="Phone number must be in the format: '+####', with 15 digits MAX.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
