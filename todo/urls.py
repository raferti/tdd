from django.urls import path
from .views import TodoListView, AddTask

urlpatterns = [
    path('', TodoListView.as_view(), name='home'),
    path('add/', AddTask.as_view(), name='add'),
]