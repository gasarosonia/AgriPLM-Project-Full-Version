# Generated by Django 5.0.7 on 2024-08-09 12:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("accounts", "0012_alter_userprofiles_title"),
        ("admin_app", "0007_notification"),
    ]

    operations = [
        migrations.CreateModel(
            name="YieldPredictions",
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
                ("yield_pred_date", models.DateTimeField(auto_now_add=True)),
                ("fertilizer_amount", models.FloatField()),
                (
                    "predicted_yield",
                    models.FloatField(blank=True, default=0.0, null=True),
                ),
                (
                    "crop_fert_pred",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="admin_app.cropfertilizerpredict",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.userprofiles",
                    ),
                ),
            ],
        ),
    ]
