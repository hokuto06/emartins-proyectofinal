from django.db import models
from django.contrib.auth.models import User
class MyTasks(models.Model):

    task_name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    task_description = models.CharField(max_length=50, null=True)
    task_content = models.TextField(max_length=150, null=True)
    deadline = models.DateTimeField()
    open = models.BooleanField(default=True) 
    
    def __str__(self):
        return f'{self.task_name}'

class TaskComments(models.Model):

    comment = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    state = models.BooleanField() #sacar este cambpo
    task_comment = models.ForeignKey(MyTasks, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.comment}'
    
class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatares', blank=True, null=True)