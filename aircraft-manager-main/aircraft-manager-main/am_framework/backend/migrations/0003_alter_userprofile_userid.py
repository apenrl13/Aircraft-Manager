# Generated by Django 5.0.3 on 2024-03-19 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0002_rename_lattitude_airporttable_latitude_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="userId",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]