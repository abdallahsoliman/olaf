# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageReceiver',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
            ],
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(to='sms.PhoneNumber'),
        ),
        migrations.AddField(
            model_name='messagereceiver',
            name='message',
            field=models.ForeignKey(to='sms.Message'),
        ),
        migrations.AddField(
            model_name='messagereceiver',
            name='receiver',
            field=models.ForeignKey(to='sms.PhoneNumber'),
        ),
    ]
