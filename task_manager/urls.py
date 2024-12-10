from django.urls import path

from task_manager import views

urlpatterns = [
    path("", views.DashboardView.as_view(), name="dashboard"),
    path("workers/<int:pk>/", views.WorkerDetailView.as_view(), name="worker_detail"),
    path("tasks/<int:pk>/", views.TaskDetailView.as_view(), name="task_detail"),
    path("tasks/create/", views.TaskCreateView.as_view(), name="create_task"),
    path("tasks/update/<int:pk>/", views.TaskUpdateView.as_view(), name="update_task"),
    path("tasks/delete/<int:pk>/", views.TaskDeleteView.as_view(), name="delete_task"),
    path("toggle-task/<int:pk>/", views.ToggleTaskStatusView.as_view(), name="toggle_task_status"),
]

app_name = "task_manager"
