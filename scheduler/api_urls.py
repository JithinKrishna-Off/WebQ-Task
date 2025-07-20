

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # keep your root view here if needed
    # API endpoints will go here, like:
    # path('tasks/', views.TaskListView.as_view(), name='task-list'),
]
