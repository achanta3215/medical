# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0005_auto_20151123_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='price',
            field=models.IntegerField(max_length=10),
        ),
    ]
