# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-10-31 07:55
from __future__ import unicode_literals

from django.db import migrations


def populate_person_identifier_from_person_email(apps, schema_editor):
    Person = apps.get_model("people", "Person")
    PersonIdentifier = apps.get_model("people", "PersonIdentifier")

    ids_to_make = []
    for person in Person.objects.exclude(email=None):
        ids_to_make.append(
            PersonIdentifier(
                person_id=person.pk, value=person.email, value_type="email"
            )
        )

    PersonIdentifier.objects.bulk_create(ids_to_make)


class Migration(migrations.Migration):

    dependencies = [("people", "0009_copy_popolo_fields_to_person_identifiers")]

    operations = [
        migrations.RunPython(
            populate_person_identifier_from_person_email,
            migrations.RunPython.noop,
        )
    ]
