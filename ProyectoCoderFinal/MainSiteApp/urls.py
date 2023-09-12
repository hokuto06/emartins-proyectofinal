from django.urls import path
from MainSiteApp import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.inicio, name="Dashboard"),
    path('user-tasks', views.tasks, name="UserTasks"),
    path('new-task', views.createTask, name="CreateTask"),
    path('delete-task/<id>', views.delete_task, name="DeleteTask"),
]