# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 08:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photography', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='tags',
            field=models.ManyToManyField(blank=True, to='photography.Tag'),
        ),
    ]