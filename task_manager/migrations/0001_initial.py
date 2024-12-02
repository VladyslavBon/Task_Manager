# Generated by Django 5.1.3 on 2024-12-02 12:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="TaskType",
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
                ("name", models.CharField(max_length=127)),
            ],
        ),
        migrations.CreateModel(
            name="Task",
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
                ("name", models.CharField(max_length=127)),
                ("description", models.TextField()),
                ("deadline", models.DateTimeField()),
                ("is_completed", models.BooleanField(default=False)),
                (
                    "priority",
                    models.CharField(
                        choices=[
                            ("Urgent", "Urgent"),
                            ("High", "High"),
                            ("Medium", "Medium"),
                            ("Low", "Low"),
                        ],
                        default="Urgent",
                        max_length=10,
                    ),
                ),
                (
                    "assignees",
                    models.ManyToManyField(
                        related_name="tasks", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "task_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tasks",
                        to="task_manager.tasktype",
                    ),
                ),
            ],
            options={
                "ordering": ["is_completed"],
            },
        ),
    ]
