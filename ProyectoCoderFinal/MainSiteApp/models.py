from django.db import models

# Create your models here.

class MyTasks(models.Model):

    task_name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    task_description = models.CharField(max_length=50, null=True)
    task_content = models.CharField(max_length=150, null=True)
    
    def __str__(self):
        return f'{self.task_name}'

class TaskComments(models.Model):

    comment = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    state = models.BooleanField()
    task_comment = models.ForeignKey(MyTasks, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.comment}'