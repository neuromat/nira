# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-11-09 20:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0007_using_modeltranslation_to_role'),
        ('configuration', '0003_removed_image_and_qr'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrincipalInvestigator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='person.Person', verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Principal Investigator',
                'permissions': (('change_principal_investigator', 'Can change the Principal Investigator.'),),
            },
        ),
    ]
