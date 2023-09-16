from django.shortcuts import render
from django.http import HttpRequest
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *

def inicio(req: HttpRequest):
 
    try:
        avatar = Avatar.objects.get(user=req.user.id)
        return render(req, 'dashboard.html', {"message":f"test","url": avatar.image.url})
    except:
        return render(req, 'dashboard.html')

def view_tasks(req):
    task_list = MyTasks.objects.all()
    return render(req, 'tasks.html', {"tasklist": task_list})

def createTask(req):

    if req.method == 'POST':
        formTask = TaskCreationForm(req.POST)
        if formTask.is_valid():
            data = formTask.cleaned_data
            newtask = MyTasks( task_name = data['task_name'], task_description = data['task_description'],
                              task_content = data['task_content'] )
            newtask.save()
            task_list = MyTasks.objects.all()
            return render(req, "tasks.html", {"tasklist": task_list})
    else:
        taskForm = TaskCreationForm()
    return render(req, "taskForm.html", {"taskForm": taskForm})

def delete_task(req, id):
    
    if req.method == 'POST':

        task = MyTasks.objects.get(id=id)
        task.delete()
        task_list = MyTasks.objects.all()

        return render(req, 'tasks.html', {'tasklist': task_list})
    
def create_comment(req: HttpRequest, id):
    taskObject = MyTasks.objects.get(id=id)

    if req.method == 'POST':
        print("Esto es metodo post")
        formComment = CommentCreationForm(req.POST)
        if formComment.is_valid():
            data = formComment.cleaned_data

            task_comment = TaskComments(comment=data['comment'],state=data['state'],task_comment=taskObject)
            task_comment.save()
            return render(req, 'tasks.html')
    
    else:
        print("esto es metodo get")
        task = MyTasks.objects.get(id=id)
        comment_form = CommentCreationForm(initial={
            "state": 1,
            "task_comment":task,
        })

        return render(req, 'commentForm.html', {"commentForm": comment_form, 'task': task})

###Clases basadas en vistas

class TaskList(ListView):
    model = MyTasks
    template_name = "list_task.html"
    # fields = '__all__'
    context_object_name = "prueba"

class TaskDetail(DetailView):
    model = MyTasks
    template_name = "task_detail.html"
    context_object_name = "task"

class CreateTask(CreateView):
    model = MyTasks
    template_name = "task_create.html"
    fields = ["task_name","task_description","deadline","task_content"]
    success_url = "/proyecto-final/list-tasks/"

class DeleteTask(DeleteView):
    model = MyTasks
    template_name = "delete_task.html"
    success_url = "/proyecto-final/list-tasks/"


##### login #####

def login_view(req: HttpRequest):

    if req.method == 'POST':

        formulario = AuthenticationForm(req, data=req.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data
            username = data["username"]
            password = data["password"]

            user = authenticate(username=username, password=password)

            if user:
                login(req, user) 
                return render(req, "dashboard.html", {"message": f"Bienvenido {username}"})
            else:
                return render(req, "dashboard.html", {"message": f"Datos incorrectos"})
        else:
            return render(req, "dashboard.html", {"message": "Datos incorrectos"})
    else:
        formulario = AuthenticationForm()
        return render(req, "login.html", {"formulario": formulario})

def register(req: HttpRequest):

    if req.method == 'POST':

        formulario = UserCreationForm(req.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data

            username = data['username']

            formulario.save()

            return render(req, "dashboard.html", {"message": f"Usuario {username} creado"})
        else:
            return render(req, "dashboard.html", {"message": "Datos incorrectos"})
    else:
        formulario = UserCreationForm()
        return render(req, "register.html", {"formulario": formulario})
    
def edit_perfil(req: HttpRequest):

    user = req.user

    if req.method == 'POST':
        formulario = UserEditForm(req.POST, instance=req.user )
    
        if formulario.is_valid():

            data = formulario.cleaned_data

            user.first_name = data['first_name']
            user.last_name = data['last_name']
            # user.email = data['email']
            user.set_password(data["password1"])
            user.save()
            return render(req, "dashboard.html", {"message": "Perfil actualizado con exito"})
        else:
            return render(req, 'edit_perfil.html', {"formulario": formulario})
    else:
        formulario = UserEditForm(instance=req.user)    
    
        return render(req, 'edit_perfil.html', {"formulario": formulario})
    
def add_avatar(req: HttpRequest):

    if req.method == 'POST':

        formulario = AvatarForm(req.POST, req.FILES)

        if formulario.is_valid():

            data = formulario.cleaned_data

            avatar = Avatar(user=req.user, image=data['image'])

            avatar.save()

            return render(req, "dashboard.html", {"message": f"Avatar actualizado con exito!"})

        else:
            return render(req, "dashboard.html", {"message": "Formulario invalido"})
        
    else:
        formulario = AvatarForm()
        return render(req, "add_avatar.html", {"formulario": formulario})