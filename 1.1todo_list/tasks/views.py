from django.views.generic.detail import SingleObjectMixin
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.views import View
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Task
from .forms import TaskForm


class TaskListView(ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("task_list")

    def form_valid(self, form):
        form.instance.completed = False
        return super().form_valid(form)


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("task_list")
    template_name = "tasks/task_confirm_delete.html"


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("task_list")


class TaskMarkDoneView(SingleObjectMixin, View):
    model = Task

    def get(self, request, *args, **kwargs):
        task = self.get_object()
        task.completed = not task.completed
        task.save()
        return redirect("task_list")
