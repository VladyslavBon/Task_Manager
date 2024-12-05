from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic, View

from accounts.models import Worker
from task_manager.forms import TaskForm
from task_manager.models import Task


class DashboardView(generic.ListView):
    model = Worker
    template_name = "task_manager/dashboard.html"
    context_object_name = "workers"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = Task.objects.select_related("task_type").prefetch_related("assignees")
        return context


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = self.object.tasks.select_related("task_type")
        return context


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_manager:dashboard")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm

    def get_success_url(self):
        return reverse_lazy("task_manager:task_detail", kwargs={"pk": self.object.pk})


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task_manager:dashboard")


class ToggleTaskStatusView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        task.is_completed = not task.is_completed
        task.save()
        return HttpResponseRedirect(request.META.get("HTTP_REFERER", reverse("task_manager:dashboard")))
