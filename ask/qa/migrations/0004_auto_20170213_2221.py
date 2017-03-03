# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0003_auto_20170213_2220'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AAnswer',
            new_name='Answer',
        ),
    ]
