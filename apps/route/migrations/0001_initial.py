# Generated by Django 4.2.4 on 2023-08-29 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Route",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=50)),
                ("description", models.TextField()),
                ("location", models.CharField(max_length=50)),
                (
                    "level",
                    models.CharField(
                        choices=[
                            ("Beginner", "Beginner"),
                            ("Intermediate", "Intermediate"),
                            ("Advanced", "Advanced"),
                        ],
                        max_length=12,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "tag_name",
                    models.CharField(
                        choices=[
                            ("chill", "chill"),
                            ("no traffic", "no traffic"),
                            ("good tar", "good tar"),
                            ("bad tar", "bad tar"),
                            ("scenic", "scenic"),
                            ("urban", "urban"),
                            ("no elevation", "no elevation"),
                            ("strong elevation", "strong elevation"),
                            ("in nature", "in nature"),
                            ("short", "short"),
                            ("long", "long"),
                            ("multiple days", "multiple days"),
                            ("downhill", "downhill"),
                        ],
                        max_length=50,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="RoutesTag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "route_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="route.route"
                    ),
                ),
                (
                    "tag_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="route.tag"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="route",
            name="tags",
            field=models.ManyToManyField(through="route.RoutesTag", to="route.tag"),
        ),
    ]
