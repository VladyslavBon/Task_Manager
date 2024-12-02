from django.test import TestCase

from task_manager.models import Task, TaskType


class TaskModelTests(TestCase):
    def test_task_string(self):
        task = Task.objects.create(
            name="test_task",
            priority="Urgent",
            task_type=TaskType.objects.create(name="Test")
        )
        self.assertEqual(
            str(task),
            f"{task.name}"
        )

    def test_task_type_string(self):
        task_type = TaskType.objects.create(
            name="test_task_type",
        )
        self.assertEqual(
            str(task_type),
            f"{task_type.name}"
        )
