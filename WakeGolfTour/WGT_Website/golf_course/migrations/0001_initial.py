# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-02 03:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GolfCourse',
            fields=[
                ('course_id', models.IntegerField(primary_key=True, serialize=False)),
                ('course_name', models.TextField()),
                ('course_total_par', models.IntegerField()),
            ],
            options={
                'managed': False,
                'verbose_name_plural': 'Golf Courses',
                'verbose_name': 'Golf Course',
                'db_table': 'GolfCourse',
            },
        ),
        migrations.CreateModel(
            name='Hole',
            fields=[
                ('hole_id', models.IntegerField(primary_key=True, serialize=False)),
                ('hole_number', models.IntegerField()),
                ('hole_par', models.IntegerField()),
            ],
            options={
                'managed': False,
                'db_table': 'Hole',
            },
        ),
    ]
