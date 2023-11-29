from django.urls import path
from .views import TaskListView, TaskCreateView, TaskDeleteView, TaskUpdateView, TaskMarkDoneView

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("add/", TaskCreateView.as_view(), name="task_add"),
    path("delete/<int:pk>/", TaskDeleteView.as_view(), name="task_delete"),
    path("update/<int:pk>/", TaskUpdateView.as_view(), name="task_update"),
    path('<int:pk>/mark_done/', TaskMarkDoneView.as_view(), name='task_mark_done'),
]
