# Generated by Django 5.0.3 on 2024-05-07 05:11

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0006_conversation_level_conversation_topic_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="conversation",
            name="topic",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=255), default=list, size=None
            ),
        ),
    ]