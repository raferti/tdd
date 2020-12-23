from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from todo.models import Task


class TodoListView(ListView):
    model = Task
    template_name = 'todo/index.html'
    context_object_name = 'tasks'


class AddTask(CreateView):
    model = Task
    fields = ('title', 'text')
    success_url = reverse_lazy('home')

