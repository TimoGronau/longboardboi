# Generated by Django 4.2.4 on 2023-08-29 12:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("route", "0003_rename_routestag_routetag"),
    ]

    operations = [
        migrations.RenameField(
            model_name="routetag",
            old_name="route_id",
            new_name="route",
        ),
        migrations.RenameField(
            model_name="routetag",
            old_name="tag_id",
            new_name="tag",
        ),
    ]
