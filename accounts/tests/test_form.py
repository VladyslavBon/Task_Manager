from django.test import TestCase

from accounts.forms import WorkerRegistrationForm
from accounts.models import Position


class WorkerFormsTest(TestCase):
    def test_worker_registration_form_with_valid_data(self):
        form_data = {
            "username": "new_user",
            "email": "test_email@test.test",
            "first_name": "Test firstname",
            "last_name": "Test lastname",
            "position": Position.objects.create(name="Test position"),
            "password1": "user12test",
            "password2": "user12test",
        }
        form = WorkerRegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
