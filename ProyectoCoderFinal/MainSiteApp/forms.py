from django import forms

class TaskCreationForm(forms.Form):

    task_name = forms.CharField()
    task_description = forms.CharField()
    task_content = forms.CharField(widget=forms.Textarea)

