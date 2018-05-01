# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fingerprint', '0005_auto_20180114_0733'),
    ]

    operations = [
        migrations.AddField(
            model_name='conference',
            name='notifytime',
            field=models.CharField(default=b'', max_length=20),
        ),
    ]
