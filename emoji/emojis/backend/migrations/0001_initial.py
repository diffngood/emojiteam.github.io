# Generated by Django 4.1.7 on 2023-03-11 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=20)),
                ("password", models.CharField(max_length=20)),
            ],
        ),
    ]
