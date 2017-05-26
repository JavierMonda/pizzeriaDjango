# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-25 11:09
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0013_auto_20170525_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='pizza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='pizzas.Pizza', verbose_name='Pizza'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='score',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)], verbose_name='Puntuación'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.CharField(max_length=140, verbose_name='Comentario'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='ingredients',
            field=models.ManyToManyField(related_name='pizzas', to='pizzas.Ingredient', verbose_name='Ingredientes'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nombre'),
        ),
    ]
