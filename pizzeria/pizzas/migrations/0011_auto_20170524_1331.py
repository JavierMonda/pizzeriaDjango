# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-24 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0010_auto_20170524_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='score',
            field=models.IntegerField(default=5, validators=[1, 2, 3, 4, 5]),
        ),
    ]