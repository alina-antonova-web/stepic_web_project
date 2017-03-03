# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0002_auto_20170213_2219'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Answer',
            new_name='AAnswer',
        ),
    ]
