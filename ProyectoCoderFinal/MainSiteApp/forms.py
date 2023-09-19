from django import forms
from .models import *
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
#from bootstrap_datepicker_plus import DatePickerInput
#from bootstrap_datepicker_plus.widgets import DateTimePickerInput

class UserRegisterForm(UserCreationForm):

    password1 = forms.CharField(
        label="Contraseña", 
        widget=forms.PasswordInput,
        strip=False,
        error_messages={'password_mismatch': 'Las contraseñas no coinciden. Por favor, inténtalo de nuevo.'}
        )
    password2 = forms.CharField(label="Repita la Contraseña", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
    
    # def clean_password2(self):

    #     print(self.cleaned_data)

    #     password2 = self.cleaned_data["password2"]
    #     if password2 != self.cleaned_data["password1"]:
    #         raise forms.ValidationError["Contraseña incorrecta"]
    #     return password2


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
        # widgets = {
        #     'deadline': DateTimePickerInput(),
        # }


class TaskCreationForm(forms.Form):

    task_name = forms.CharField()
    task_description = forms.CharField()
    task_content = forms.CharField(widget=forms.Textarea)

class CommentCreationForm(forms.Form):

    comment = forms.CharField(widget=forms.Textarea)
    state = forms.BooleanField()
    # task_comment = forms.CharField()
    task_comment = forms.ModelChoiceField(queryset=TasksList.objects.all())

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
    