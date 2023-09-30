from django.urls import path
from django.views.generic import TemplateView
from MainSiteApp import views
from django.contrib.auth.views import LogoutView
from django.conf.urls import handler404

from .views import *

handler404 = error_404_view

urlpatterns = [
    # path('', views.inicio, name="Dashboard"),
    path('', AllTaskView.as_view(), name="Dashboard"),
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
    path('edit-avatar/', edit_avatar, name="EditAvatar"),
    path('about/', TemplateView.as_view(template_name='about.html'), name='About'),
    path('help/', help, name='Help'),
    # Mensajeria
    path('enviar-mensaje/', views.enviar_mensaje, name='enviar_mensaje'),    
    path('conversations/', views.conversation_list, name='conversation_list'),
    path('conversation/<int:conversation_id>/', views.conversation_detail, name='conversation_detail'),
    path('update_comment_state/<int:comment_id>/<str:comment_state>/', update_comment_state, name='update_comment_state'),
]
