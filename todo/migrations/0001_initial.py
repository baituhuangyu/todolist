# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('statue', models.CharField(default=b'1', max_length=2)),
                ('pubtime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['pubtime', 'statue', 'id'],
            },
        ),
    ]
