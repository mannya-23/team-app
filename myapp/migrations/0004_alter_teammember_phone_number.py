# Generated by Django 5.1.5 on 2025-01-28 17:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0003_alter_teammember_phone_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="teammember",
            name="phone_number",
            field=models.CharField(
                blank=True,
                max_length=17,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
                        regex="^\\+?1?\\d{9,15}$",
                    )
                ],
            ),
        ),
    ]
