# Generated by Django 5.1.5 on 2025-01-31 06:39

import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0010_alter_teammember_phone_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="teammember",
            name="phone_number",
            field=phonenumber_field.modelfields.PhoneNumberField(
                max_length=128, region=None
            ),
        ),
    ]
