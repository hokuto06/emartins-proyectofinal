from django.urls import path
from MainSiteApp import views
from django.contrib.auth.views import LoginView

urlpatterns = [

    path('', views.inicio, name="Dashboard"),
    path('user-tasks', views.tasks, name="UserTasks"),
]