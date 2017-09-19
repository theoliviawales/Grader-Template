# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-19 04:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('total_score', models.IntegerField()),
                ('instructions', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField()),
                ('comment', models.CharField(max_length=256)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grader.Assignment')),
            ],
        ),
    ]
