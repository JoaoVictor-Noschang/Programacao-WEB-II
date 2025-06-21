from django.contrib import admin
from django.urls import path

from todos.views import TodoListView, TodoCreateView, TodoUpdateView, TodoDeleteView, TodoCompleteView
from todos.services import TodoService
from todos.models import Todo

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TodoListView.as_view(), name="todo_list"),
    path("create", TodoCreateView.as_view(), name="todo_create"),
    path("update/<int:pk>", TodoUpdateView.as_view(), name="todo_update"),
    path("delete/<int:pk>", TodoDeleteView.as_view(), name="todo_delete"),
    # Alterado a partir daqui -------------------------------------------------------------------------------------
    path("todo/<int:pk>/complete/", TodoCompleteView.as_view(todo_service=TodoService(Todo)), name="todo_complete"),
]
