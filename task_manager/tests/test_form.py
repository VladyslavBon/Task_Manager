from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase

from accounts.models import Position
from task_manager.forms import TaskForm
from task_manager.models import TaskType


class TaskFormsTest(TestCase):
    def test_task_creation_form_with_valid_data(self):
        worker = get_user_model().objects.create_user(
            username="test_username",
            password="test123",
            first_name="test_first_name",
            last_name="test_last_name",
            position=Position.objects.create(name="Test Position"),
        ),
        task_type = TaskType.objects.create(name="Test")
        form_data = {
            "name": "test_task",
            "description": "test description",
            "deadline": datetime.now().strftime("%Y-%m-%d"),
            "priority": "Urgent",
            "task_type": task_type.id,
            "assignees": [worker[0].id]
        }

        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())

        cleaned_data = form.cleaned_data
        self.assertEqual(cleaned_data["name"], form_data["name"])
        self.assertEqual(cleaned_data["description"], form_data["description"])
        self.assertEqual(
            cleaned_data["deadline"].strftime("%Y-%m-%d"),
            form_data["deadline"]
        )
        self.assertEqual(cleaned_data["priority"], form_data["priority"])
        self.assertEqual(cleaned_data["task_type"], task_type)
