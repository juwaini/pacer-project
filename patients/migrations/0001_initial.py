# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 07:06
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('id_number', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('sex', models.CharField(max_length=1)),
                ('parent_name', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(max_length=100), size=None)),
                ('parent_email', django.contrib.postgres.fields.ArrayField(base_field=models.EmailField(max_length=254), size=None)),
                ('parent_contact_number', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), size=None)),
                ('language', models.CharField(max_length=1)),
                ('address', models.TextField()),
                ('postcode', models.CharField(max_length=10)),
                ('town', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
