# Generated by Django 4.2 on 2023-05-01 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("subscribe", "0003_subscription_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subscription",
            name="options",
            field=models.CharField(
                choices=[("W", "Weekly"), ("M", "Monthly")], default="M", max_length=2
            ),
        ),
    ]
