# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-28 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0007_auto_20180928_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='image/'),
        ),
    ]
