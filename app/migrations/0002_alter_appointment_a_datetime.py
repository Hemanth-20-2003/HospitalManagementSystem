# Generated by Django 4.2.6 on 2024-04-16 08:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointment",
            name="A_DATETIME",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime(2024, 4, 16, 8, 40, 1, 77365)
            ),
        ),
    ]