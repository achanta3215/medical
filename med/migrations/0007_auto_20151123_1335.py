# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0006_auto_20151123_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phno',
            field=models.BigIntegerField(),
        ),
    ]
