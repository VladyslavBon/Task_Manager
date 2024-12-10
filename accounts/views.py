from django.urls import reverse_lazy
from django.views import generic

from accounts.forms import WorkerRegistrationForm


class RegisterView(generic.CreateView):
    form_class = WorkerRegistrationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("task_manager:dashboard")
