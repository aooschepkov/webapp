# Generated by Django 4.2.7 on 2023-12-07 19:19

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Workout",
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
                ("start_time", models.DateTimeField()),
                ("end_time", models.DateTimeField()),
                ("exercise_name", models.CharField(max_length=100)),
                ("sets", models.IntegerField()),
                ("repetitions", models.IntegerField()),
                ("weight", models.FloatField()),
            ],
        ),
    ]
