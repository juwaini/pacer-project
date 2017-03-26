# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 07:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.TextField()),
                ('fullname', models.TextField(max_length=150)),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('doctor', 'Doctor'), ('nurse', 'Nurse'), ('parent', 'Parent'), ('patient', 'Patient'), ('norole', 'No Role')], default='norole', max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
