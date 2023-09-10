from django.shortcuts import render
from django.http import HttpRequest
from .models import *
from .forms import *

def inicio(req):
    return render(req, 'dashboard.html')

def tasks(req):
    task_list = MyTasks.objects.all()
    return render(req, 'tasks.html', {"tasklist": task_list})

def createTask(req):

    if req.method == 'POST':
        
        formTask = TaskCreationForm(req.POST)
        if formTask.is_valid:
            print('prueba'*3)
            print(formTask)
            
            data = formTask.cleaned_data
            newtask = MyTasks( task_name = data['task_name'], task_description = data['task_description'],
                              task_content = ['task_content'] )
            newtask.save()
            task_list = MyTasks.objects.all()
            return render(req, "tasks.html", {"tasklist": task_list})

    else:

        formTask = TaskCreationForm()
    return render(req, "taskForm.html", {"taskForm": formTask})