from django.test import TestCase
from django.urls import reverse

from accounts.models import Position, Worker
from task_manager.models import Task, TaskType


class ViewTest(TestCase):
    def setUp(self):
        position = Position.objects.create(name="Developer")
        self.worker = Worker.objects.create_user(
            username="worker1",
            password="test123",
            position=position
        )
        self.task_type = TaskType.objects.create(name="Bug Fix")
        self.task = Task.objects.create(
            name="Fix issue",
            description="Fixing a critical bug",
            deadline="2024-12-10",
            priority="Urgent",
            task_type=self.task_type
        )
        self.task.assignees.add(self.worker)

    def test_dashboard_view(self):
        self.client.login(username="worker1", password="test123")
        response = self.client.get(reverse("task_manager:dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "task_manager/dashboard.html")
        self.assertIn("workers", response.context)
        self.assertIn("tasks", response.context)
        self.assertEqual(len(response.context["workers"]), 1)
        self.assertEqual(len(response.context["tasks"]), 1)

    def test_worker_detail_view(self):
        self.client.login(username="worker1", password="test123")
        response = self.client.get(reverse("task_manager:worker_detail", kwargs={"pk": self.worker.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertIn("tasks", response.context)
        self.assertEqual(len(response.context["tasks"]), 1)

    def test_task_detail_view(self):
        self.client.login(username="worker1", password="test123")
        response = self.client.get(reverse("task_manager:task_detail", kwargs={"pk": self.task.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "task_manager/task_detail.html")
        self.assertEqual(response.context["task"], self.task)

    def test_task_create_view(self):
        self.client.login(username="worker1", password="test123")
        form_data = {
            "name": "New Task",
            "description": "A newly created task",
            "deadline": "2024-12-25",
            "priority": "Low",
            "task_type": self.task_type.pk,
            "assignees": [self.worker.pk]
        }
        response = self.client.post(reverse("task_manager:create_task"), data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(name="New Task").exists())

    def test_task_update_view(self):
        self.client.login(username="worker1", password="test123")
        updated_data = {
            "name": "Updated Task",
            "description": "Updated description",
            "deadline": "2024-12-15",
            "priority": "High",
            "task_type": self.task_type.pk,
            "assignees": [self.worker.pk]
        }
        response = self.client.post(reverse("task_manager:update_task", kwargs={"pk": self.task.pk}), data=updated_data)
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertEqual(self.task.name, "Updated Task")
        self.assertEqual(self.task.description, "Updated description")
        self.assertEqual(self.task.priority, "High")
        self.assertEqual(self.task.deadline.strftime("%Y-%m-%d"), "2024-12-15")

    def test_task_delete_view(self):
        self.client.login(username="worker1", password="test123")
        response = self.client.post(reverse("task_manager:delete_task", kwargs={"pk": self.task.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(pk=self.task.pk).exists())

    def test_toggle_task_status(self):
        self.client.login(username="worker1", password="test123")
        response = self.client.post(reverse("task_manager:toggle_task_status", kwargs={"pk": self.task.pk}))
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertTrue(self.task.is_completed)
