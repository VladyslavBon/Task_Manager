from django.contrib.auth.forms import UserCreationForm

from accounts.models import Worker


class WorkerRegistrationForm(UserCreationForm):
    class Meta:
        model = Worker
        fields = UserCreationForm.Meta.fields + (
            "email",
            "first_name",
            "last_name",
            "position",
        )
