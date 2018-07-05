# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-05-31 15:09
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import popolo.behaviors.models


class Migration(migrations.Migration):

    dependencies = [
        ('popolo', '0005_set_post_election_not_null_'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='membership',
            unique_together={('person', 'post_election')},
        ),
    ]
