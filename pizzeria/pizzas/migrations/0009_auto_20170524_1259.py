# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-24 12:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0008_auto_20170524_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pizza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='pizzas.Pizza'),
        ),
    ]
