# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-24 11:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0006_auto_20170524_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pizza',
            field=models.ManyToManyField(related_name='comments', to='pizzas.Pizza'),
        ),
    ]