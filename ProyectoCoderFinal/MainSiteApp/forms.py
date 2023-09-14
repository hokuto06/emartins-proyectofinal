from django import forms
from .models import *

class TaskCreationForm(forms.Form):

    task_name = forms.CharField()
    task_description = forms.CharField()
    task_content = forms.CharField(widget=forms.Textarea)

class CommentCreationForm(forms.Form):

    comment = forms.CharField(widget=forms.Textarea)
    state = forms.BooleanField()
    # task_comment = forms.CharField()
    task_comment = forms.ModelChoiceField(queryset=MyTasks.objects.all())

