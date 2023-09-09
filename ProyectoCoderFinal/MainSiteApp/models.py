from django.db import models

# Create your models here.

class MyTasks(models.Model):

    task_name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    task_description = models.CharField(max_length=50, null=True)
    task_content = models.CharField(max_length=150, null=True)
