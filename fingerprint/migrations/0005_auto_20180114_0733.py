# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fingerprint', '0004_remove_paper_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paper',
            old_name='auther',
            new_name='author',
        ),
    ]
