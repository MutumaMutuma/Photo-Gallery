# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-27 13:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0003_auto_20180927_1548'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['-pub_date_posted']},
        ),
        migrations.RenameField(
            model_name='image',
            old_name='pub_date',
            new_name='pub_date_posted',
        ),
    ]
