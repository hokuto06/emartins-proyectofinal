from django.urls import path
from MainSiteApp import views
from django.contrib.auth.views import LoginView
from .views import *
#test
urlpatterns = [
    path('', views.inicio, name="Dashboard"),
    path('user-tasks', views.view_tasks, name="UserTasks"),
    path('new-task', createTask, name="CreateTask"),
    path('delete-task/<int:id>', delete_task, name="DeleteTask"),
]