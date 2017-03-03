# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='author',
        ),
        migrations.RemoveField(
            model_name='question',
            name='author',
        ),
        migrations.RemoveField(
            model_name='question',
            name='likes',
        ),
    ]
