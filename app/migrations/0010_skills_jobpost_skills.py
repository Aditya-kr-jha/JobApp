# Generated by Django 4.2 on 2023-04-28 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0009_rename_degisnation_author_designation"),
    ]

    operations = [
        migrations.CreateModel(
            name="Skills",
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
                ("name", models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name="jobpost",
            name="skills",
            field=models.ManyToManyField(to="app.skills"),
        ),
    ]
