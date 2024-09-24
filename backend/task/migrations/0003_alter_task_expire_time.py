# Generated by Django 5.1.1 on 2024-09-20 13:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("task", "0002_alter_task_expire_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="expire_time",
            field=models.DateTimeField(
                blank=True,
                default=datetime.datetime(1, 9, 20, 16, 41, 46, 325866),
                null=True,
            ),
        ),
    ]
