from django import forms
from .models import *
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].error_messages = {'unique': 'El usuario ya existe.'}

    password1 = forms.CharField(
        label="Contraseña", 
        widget=forms.PasswordInput,
        strip=False,
    )
    password2 = forms.CharField(
        label="Repita la Contraseña",
        widget=forms.PasswordInput,
    )
    error_messages = {
        'password_mismatch': 'Las contraseñas no coinciden. Inténtelo nuevamente.',
    }
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        help_texts = {k: "" for k in fields}


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = TasksList
        fields = ['task_name', 'task_description', 'deadline', 'task_content']
        labels = {
            'task_name': "Nombre",
            'task_description': 'Descripcion',
            'deadline' : 'Fecha de finalizacion',
            'task_content': 'Contenido',
        }
        widgets = {
            'deadline': forms.TextInput(attrs={'type': 'datetime-local'}),
        }

class TasksListForm(forms.ModelForm):
    class Meta:
        model = TasksList
        fields = ['task_name', 'task_description', 'task_content', 'deadline', 'open']
        widgets = {
            'deadline': forms.TextInput(attrs={'type': 'datetime-local'}),
        }

# class TaskCreationForm(forms.Form):

#     task_name = forms.CharField()
#     task_description = forms.CharField()
#     task_content = forms.CharField(widget=forms.Textarea)

class CommentCreationForm(forms.Form):

    comment = forms.CharField(widget=forms.Textarea)
    state = forms.BooleanField(widget=forms.HiddenInput(), initial=True)
    task_comment = forms.ModelChoiceField(widget=forms.HiddenInput(),queryset=TasksList.objects.all())

class UserEditForm(UserChangeForm):

    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita la Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields=('first_name', 'last_name')

    def clean_password2(self):

        print(self.cleaned_data)

        password2 = self.cleaned_data["password2"]
        if password2 != self.cleaned_data["password1"]:
            raise forms.ValidationError("Las contraseñas no coinciden...")
        return password2

class AvatarForm(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ('image',)
    