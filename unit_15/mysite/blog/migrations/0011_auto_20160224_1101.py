# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-24 11:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20160223_1315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='entry',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
