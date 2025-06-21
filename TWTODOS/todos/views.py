from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy

from django.shortcuts import redirect
from .models import Todo
from .services import TodoService  # Importa o serviço

class TodoListView(ListView):
    model = Todo

class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")


class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")


class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")


class TodoCompleteView(View):
    todo_service = None  # Adicionamos o atributo esperado

    def dispatch(self, request, *args, **kwargs):
        if self.todo_service is None:
            self.todo_service = TodoService(Todo)  # Definimos o serviço padrão
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, pk):
        self.todo_service.mark_as_complete(pk)
        return redirect("todo_list")