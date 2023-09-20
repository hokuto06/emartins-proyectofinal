from django.urls import path
from django.views.generic import TemplateView
from MainSiteApp import views

from django.contrib.auth.views import LogoutView
from .views import *
#test
urlpatterns = [
    path('', views.inicio, name="Dashboard"),
    #path('list-tasks/', view_tasks, name="ListTasks"),
    # path('new-task', createTask, name="CreateTask"),
    #path('delete-task/<int:id>', delete_task, name="DeleteTask"),
    path('create-comment/<int:id>', create_comment, name="CreateComment"),
    # path('create-comment/<int:pk>', CreateTasksListRow.as_view(), name="CreateComment"),
    #path('create-comment/<int:pk>/', CreateTasksListRow.as_view(), name='CreateComment'),
    # path('create-comment', CreateTasksListRow.as_view(), name='CreateComment'),

    path('view-comments/<int:id>', view_comments, name="ViewComments"),
    path('list-tasks/', TaskList.as_view(), name="ListTasks"),
    path('detail-tasks/<pk>', TaskDetail.as_view(), name="DetailTasks"),
    path('create-task', CreateTask.as_view(), name="CreateTask"),
    path('delete-task/<pk>', DeleteTask.as_view(), name="DeleteTask"),
    path('login/', login_view, name="Login"),
    path('register', register, name="Register"),
    path('logout/', LogoutView.as_view(next_page="Login"), name="Logout"),
    # path('logout/', LogoutView.as_view(template_name="dashboard.html"), name="Logout"),
    path('edit-perfil/', edit_perfil, name="EditPerfil"),
    path('add-avatar/', add_avatar, name="AddAvatar"),
    path('about/', TemplateView.as_view(template_name='about.html'), name='About'),
    # Mensajeria
    path('send_message/<int:user_id>/', views.send_message, name='send_message'),
    path('view_messages/<int:sender_id>/<int:receiver_id>/', views.view_messages, name='view_messages'),


]
