# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', null=True, blank=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, db_index=True, unique=True)),
                ('phone_number', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message="Phone number must be in the format: '+####', with 15 digits MAX.", regex='^\\+?1?\\d{9,15}$')], blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
