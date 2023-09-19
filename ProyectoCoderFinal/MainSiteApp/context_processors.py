import datetime
from django.http import HttpRequest, HttpResponse
from .models import Avatar, TasksList

def get_current_year(req):
    current_year = datetime.datetime.now().year

    return {
        "current_year": current_year
    }

def load_avatar(req: HttpRequest):
    try:
        avatar = Avatar.objects.get(user=req.user.id)
        return {"url": avatar.image.url}
    except:
        image_data = open("media/avatares/goku.jpg", "rb").read()
        return {"url": image_data}

def count_tasks_owner(req: HttpRequest):
    try:
        count_tasks = TasksList.objects.filter(owner=req.user).count()
        return {"count_tasks": count_tasks}
    except:
        count_tasks = 0
        return {"count_tasks": count_tasks}