# Generated by Django 4.2 on 2023-04-22 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_jobpost_date_jobpost_discription_jobpost_salary'),
    ]

    operations = [
        migrations.RenameField(
            'jobpost', 'discription', 'description'),
    ]
