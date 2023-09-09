from django.shortcuts import render
from django.http import HttpRequest

def inicio(req):
    return render(req, 'index.html')
