from django.contrib.auth import get_user_model
from django.test import TestCase

from accounts.models import Position


class WorkerModelTests(TestCase):
    def test_worker_string(self):
        worker = get_user_model().objects.create_user(
            username="test_username",
            password="test123",
            first_name="test_first_name",
            last_name="test_last_name",
            position=Position.objects.create(name="Test Position"),
        )
        self.assertEqual(
            str(worker),
            f"{worker.username} ({worker.first_name} {worker.last_name})"
        )

    def test_create_task_with_assignee(self):
        username = "test_username"
        password = "test123"
        worker = get_user_model().objects.create_user(
            username=username,
            password=password,
            position=Position.objects.create(name="Test Position"),
        )
        self.assertEqual(worker.username, username)
        self.assertTrue(worker.check_password(password))

    def test_task_type_string(self):
        position = Position.objects.create(
            name="Test Position",
        )
        self.assertEqual(
            str(position),
            f"{position.name}"
        )
