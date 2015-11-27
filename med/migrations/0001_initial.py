# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('bid', models.IntegerField(serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bid', models.ForeignKey(to='med.Bill')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cname', models.CharField(max_length=20)),
                ('cid', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('phno', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Medicines',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mid', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='mid',
            field=models.ForeignKey(to='med.Medicines'),
        ),
        migrations.AddField(
            model_name='bill',
            name='cid',
            field=models.ForeignKey(to='med.Customer'),
        ),
        migrations.AlterUniqueTogether(
            name='cart',
            unique_together=set([('bid', 'mid')]),
        ),
    ]
