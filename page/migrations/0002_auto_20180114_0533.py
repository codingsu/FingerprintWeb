# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='pager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('auther', models.CharField(default=b'', max_length=100)),
                ('title', models.CharField(default=b'', max_length=100)),
                ('conferencename', models.CharField(default=b'', max_length=100)),
                ('publishdate', models.CharField(default=b'', max_length=100)),
                ('filename', models.CharField(default=b'', max_length=150)),
                ('level', models.CharField(default=b'', max_length=10)),
                ('url', models.CharField(default=b'', max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='conference',
            name='asfasdf',
        ),
    ]
