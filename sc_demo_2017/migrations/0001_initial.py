# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-20 17:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NVDIMM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bw', models.DecimalField(decimal_places=2, default='x', max_digits=10)),
                ('lat', models.DecimalField(decimal_places=2, default='x', max_digits=10)),
                ('iops', models.DecimalField(decimal_places=2, default='x', max_digits=10)),
            ],
        ),
    ]