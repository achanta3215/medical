# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0007_auto_20151123_1335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicine',
            name='id',
        ),
        migrations.AlterField(
            model_name='medicine',
            name='mid',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
