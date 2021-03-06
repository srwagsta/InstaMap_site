# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 14:23
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorldMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default='None')),
                ('id_code', models.TextField(default='None')),
                ('lat', models.FloatField(default='43.065019', max_length=20)),
                ('lon', models.FloatField(default='-87.878286', max_length=20)),
                ('tags', models.TextField(default='None')),
                ('link', models.TextField(default='None')),
                ('image_url', models.TextField(default='None')),
                ('loc_name', models.TextField(default='None')),
                ('loc_point', django.contrib.gis.db.models.fields.PointField(default='SRID=4326;POINT(0.0 0.0)', srid=4326)),
            ],
        ),
    ]
