# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_auto_20180114_0551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paper',
            name='url',
        ),
    ]
