# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-26 11:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0026_auto_20160425_1501'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='talkproposal',
            options={'verbose_name': 'talk proposal', 'verbose_name_plural': 'talk proposals'},
        ),
        migrations.AlterModelOptions(
            name='tutorialproposal',
            options={'verbose_name': 'tutorial proposal', 'verbose_name_plural': 'tutorial proposals'},
        ),
    ]