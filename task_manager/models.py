from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.models import Worker


class TaskType(models.Model):
    name = models.CharField(max_length=127)

    def __str__(self):
        return self.name


class Task(models.Model):
    Priority = [
        ("Urgent", "Urgent"),
        ("High", "High"),
        ("Medium", "Medium"),
        ("Low", "Low")
    ]

    name = models.CharField(max_length=127)
    description = models.TextField(blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, choices=Priority, default="Urgent")
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE, related_name="tasks")
    assignees = models.ManyToManyField(Worker, related_name="tasks")

    class Meta:
        ordering = ["is_completed"]

    def __str__(self):
        return self.name
