# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='conference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100)),
                ('startdate', models.CharField(default=b'', max_length=20)),
                ('level', models.CharField(default=b'', max_length=10)),
                ('deadline', models.CharField(default=b'', max_length=20)),
                ('location', models.CharField(default=b'', max_length=20)),
                ('url', models.CharField(default=b'', max_length=200)),
                ('asfasdf', models.CharField(default=b'', max_length=200)),
                ('filename', models.CharField(default=b'', max_length=150)),
            ],
        ),
    ]
