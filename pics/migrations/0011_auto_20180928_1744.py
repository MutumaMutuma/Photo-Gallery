# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-28 14:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0010_auto_20180928_1743'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='category',
        ),
        migrations.AddField(
            model_name='image',
            name='category',
            field=models.ManyToManyField(to='pics.Category'),
        ),
    ]