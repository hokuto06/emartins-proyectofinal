import datetime
from django.http import HttpRequest, HttpResponse
from .models import Avatar

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