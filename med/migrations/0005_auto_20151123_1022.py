# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0004_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='id',
        ),
        migrations.AlterField(
            model_name='staff',
            name='username',
            field=models.CharField(max_length=20, serialize=False, primary_key=True),
        ),
    ]
