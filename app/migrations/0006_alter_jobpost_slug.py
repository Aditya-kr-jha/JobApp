# Generated by Django 4.2 on 2023-04-23 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_rename_discription_jobpost_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobpost",
            name="slug",
            field=models.SlugField(max_length=40, null=True, unique=True),
        ),
    ]
