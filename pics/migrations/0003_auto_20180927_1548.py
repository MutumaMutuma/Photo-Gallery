# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-27 12:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='gallery/')),
                ('image_url', models.TextField()),
                ('image_name', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=100)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('category', models.ManyToManyField(to='pics.Category')),
            ],
        ),
        migrations.RenameField(
            model_name='location',
            old_name='name',
            new_name='location',
        ),
        migrations.AddField(
            model_name='image',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pics.Location'),
        ),
    ]
