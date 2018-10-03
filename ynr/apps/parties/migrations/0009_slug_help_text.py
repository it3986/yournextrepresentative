# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-10-03 18:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("parties", "0008_unique_ec_id")]

    operations = [
        migrations.AlterField(
            model_name="party",
            name="legacy_slug",
            field=models.CharField(
                blank=True,
                help_text="\n            A slug used in URLs that comes from the old OrganizationExtra model. \n            This field will be removed in the future in favour of the ec_id, \n            but it's required until then",
                max_length=256,
                unique=True,
            ),
        )
    ]
