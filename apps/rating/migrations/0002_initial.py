# Generated by Django 4.2.4 on 2023-08-29 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("rating", "0001_initial"),
        ("route", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="rating",
            name="route_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="route.route"
            ),
        ),
    ]
