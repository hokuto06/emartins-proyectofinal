from django.shortcuts import render
from django.http import HttpRequest
from .models import *

def inicio(req):
    return render(req, 'dashboard.html')

def tasks(req):
    task_list = MyTasks.objects.all()
    return render(req, 'tasks.html', {"tasklist": task_list})