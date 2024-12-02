from django.contrib.auth import login
from django.shortcuts import render, redirect

from accounts.forms import WorkerRegistrationForm


def register(request):
    if request.method == "POST":
        form = WorkerRegistrationForm(request.POST)
        if form.is_valid():
            worker = form.save()
            login(request, worker)
            return redirect("task_manager:dashboard")
    else:
        form = WorkerRegistrationForm()
    return render(request, "registration/register.html", {"form": form})
