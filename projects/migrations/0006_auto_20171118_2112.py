# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-19 03:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20171104_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(default=None, upload_to='project_images'),
        ),
        migrations.AlterField(
            model_name='project',
            name='repository',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='website',
            field=models.TextField(blank=True, default=''),
        ),
    ]
