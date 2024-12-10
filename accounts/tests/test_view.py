from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from accounts.models import Position


class AuthViewsTests(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="Manager")
        self.user_data = {
            "username": "testuser",
            "password": "testpassword123",
            "first_name": "Test",
            "last_name": "User",
            "email": "testuser@example.com",
            "position": self.position,
        }
        self.user = get_user_model().objects.create_user(
            username=self.user_data["username"],
            password=self.user_data["password"],
            first_name=self.user_data["first_name"],
            last_name=self.user_data["last_name"],
            email=self.user_data["email"],
            position=self.position,
        )

    def test_login_view(self):
        response = self.client.get(reverse("accounts:login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/login.html")

        response = self.client.post(
            reverse("accounts:login"),
            {"username": self.user_data["username"], "password": self.user_data["password"]},
        )
        self.assertRedirects(response, reverse("task_manager:dashboard"))

        response = self.client.post(
            reverse("accounts:login"),
            {"username": "wronguser", "password": "wrongpassword"},
        )
        self.assertContains(response, "Please enter a correct username and password.")

    def test_logout_view(self):
        self.client.login(username=self.user_data["username"], password=self.user_data["password"])

        response = self.client.post(reverse("accounts:logout"))
        self.assertRedirects(response, reverse("accounts:login"))

    def test_register_view(self):
        response = self.client.get(reverse("accounts:register"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/register.html")

        new_user_data = {
            "username": "newuser",
            "password1": "newpassword123",
            "password2": "newpassword123",
            "first_name": "New",
            "last_name": "User",
            "email": "newuser@example.com",
            "position": self.position.id,
        }
        response = self.client.post(reverse("accounts:register"), new_user_data)
        self.assertRedirects(response, reverse("task_manager:dashboard"))

        self.assertTrue(get_user_model().objects.filter(username="newuser").exists())
