# Generated by Django 5.0.7 on 2024-08-09 13:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("farmer_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="yieldpredictions",
            name="is_project_active",
            field=models.BooleanField(default=False),
        ),
    ]
