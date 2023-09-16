from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(MyTasks)
admin.site.register(TaskComments)
admin.site.register(Avatar)