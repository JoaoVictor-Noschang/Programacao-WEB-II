from django.shortcuts import get_object_or_404
from .models import Todo

class TodoService:
    def __init__(self, model=None):
        self.model = model or Todo

    def mark_as_complete(self, pk):
        todo = get_object_or_404(self.model, pk=pk)
        todo.mark_has_complete()
        return todo
