from django.db import models
from django.contrib.auth.models import User


class TasksList(models.Model):

    task_name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    task_description = models.CharField(max_length=50, null=True)
    task_content = models.TextField(max_length=150, null=True)
    deadline = models.DateTimeField()
    open = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.task_name}'

class TasksListRows(models.Model):

    comment = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    state = models.BooleanField() # Este campo debio llamarse "Open" 
    task_comment = models.ForeignKey(TasksList, on_delete=models.CASCADE)
    date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.comment}'

# Creacion y Edicion de Avatar
class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatares', blank=True, null=True)

# Modelos Mensajeria 
class Conversation(models.Model):
    participants = models.ManyToManyField(User, related_name='conversations')

class Message(models.Model):
    text = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
