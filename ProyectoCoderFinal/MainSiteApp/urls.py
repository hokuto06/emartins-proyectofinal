from django.urls import path
from MainSiteApp import views
from django.contrib.auth.views import LogoutView
from .views import *
#test
urlpatterns = [
    path('', views.inicio, name="Dashboard"),
    path('user-tasks', views.view_tasks, name="UserTasks"),
    # path('new-task', createTask, name="CreateTask"),
    #path('delete-task/<int:id>', delete_task, name="DeleteTask"),
    path('create-comment/<int:id>', create_comment, name="CreateComment"),
    path('list-tasks/', TaskList.as_view(), name="ListTasks"),
    path('detail-tasks/<pk>', TaskDetail.as_view(), name="DetailTasks"),
    path('create-task', CreateTask.as_view(), name="CreateTask"),
    path('delete-task/<pk>', DeleteTask.as_view(), name="DeleteTask"),
    path('login/', login_view, name="Login"),
    path('register', register, name="Register"),
    path('logout/', LogoutView.as_view(template_name="dashboard.html"), name="Logout"),
]