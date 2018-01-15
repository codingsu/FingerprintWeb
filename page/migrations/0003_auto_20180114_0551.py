# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_auto_20180114_0533'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='pager',
            new_name='paper',
        ),
    ]
