# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 12:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_auto_20170330_0508'),
        ('diagnostics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnostic',
            name='diagnostic_for',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='patients.Patient'),
            preserve_default=False,
        ),
    ]
