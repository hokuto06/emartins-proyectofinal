from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
#from .models import Conversation, Message
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import itertools

from .models import *
from .forms import *
from .utils import get_user_color

@login_required
def inicio(req: HttpRequest):
 
    try:
        avatar = Avatar.objects.get(user=req.user.id)
        return render(req, 'dashboard.html', {"message":f"test","url": avatar.image.url})
    except:
        return render(req, 'dashboard.html')

def delete_task(req: HttpRequest, id):
    if req.method == 'POST':
        task = TasksList.objects.get(id=id)
        if task.owner == req.user:
            task.delete()
            task_list = TasksList.objects.all()

            return render(req, 'tasks.html', {'tasklist': task_list})
        else:
            return render(req, '404.html', status=404)

def create_comment(req, id):
    taskObject = TasksList.objects.get(id=id)

    if req.method == 'POST':
        formComment = CommentCreationForm(req.POST)
        if formComment.is_valid():
            data = formComment.cleaned_data 
            # El estado (open o close) siempre es 0 
            task_comment = TasksListRows(comment=data['comment'], state=0, task_comment=taskObject) 
            task_comment.save()
            return redirect('DetailTasks', pk=id)
    
    else:
        task = TasksList.objects.get(id=id)
        comment_form = CommentCreationForm(initial={
            "state": 1, # Envio el valor del bolean como True pq me da error si es 0 error, no se corrige por tiempo de entrega. 
            "task_comment": task,
        })

        return render(req, 'commentForm.html', {"commentForm": comment_form, 'task': task})


def view_comments(req: HttpRequest, id):
    comment_list = TasksListRows.objects.filter(task_comment__id=id)
    print(comment_list)
    return render(req, 'task_comment.html', {'comment_list': comment_list})

###Clases basadas en vistas

class AllTaskView(LoginRequiredMixin, ListView):
    model = TasksList
    template_name = "dashboard.html"
    context_object_name = "lists"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Obtén todas las tareas
        tasks = TasksList.objects.all()

        # Agrupar tareas por propietario (owner)
        tasks_by_owner = {}
        tasks = sorted(tasks, key=lambda task: task.owner.id)

        for owner_id, task_group in itertools.groupby(tasks, key=lambda task: task.owner.id):
            tasks_by_owner[owner_id] = list(task_group)

        context['tasks_by_owner'] = tasks_by_owner  # Pasar las tareas agrupadas al contexto
        print(context['tasks_by_owner'])
        return context

class TaskList(LoginRequiredMixin, ListView):
    model = TasksList
    template_name = "task_list.html"
    paginate_by = 3
    # fields = '__all__'
    context_object_name = "prueba"
    def get_queryset(self):
        query = self.request.GET.get('q')
        queryset = super().get_queryset().filter(owner=self.request.user)
        if query:
            queryset = queryset.filter(task_name__icontains=query)
        return queryset        
        # return super().get_queryset().filter(owner=self.request.user)


class TaskDetail(DetailView):

    model = TasksList
    template_name = "task_detail.html"
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        task = self.object
        rows = task.taskslistrows_set.all()
        allrows = TasksListRows.objects.all()
        for taskrow in allrows:
            if taskrow.comment == 'Implementacion de Nh City':
                print(f'\nEstado: {taskrow.state} - Tarea: {taskrow.comment}\n')
        print(allrows)
        total_rows = rows.count()
        context['comentarios'] = rows
        context['total_rows'] = total_rows        
        return context


#pasar owner id
class CreateTask(CreateView):
    
    model = TasksList
    template_name = "task_create.html"
    #fields = ["task_name","task_description","deadline","task_content"]
    success_url = "/proyecto-final/list-tasks/"
   
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CreateTask, self).form_valid(form)

    def get_form_class(self):
        return CreateTaskForm

class DeleteTask(DeleteView):
    model = TasksList
    template_name = "delete_task.html"
    success_url = "/proyecto-final/list-tasks/"


##### login #####

def login_view(req: HttpRequest):

    if req.method == 'POST':

        formulario = AuthenticationForm(req, data=req.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data
            username = data["username"]
            password = data["password"]

            user = authenticate(username=username, password=password)

            if user:
                login(req, user) 
                return render(req, "dashboard.html", {"message": f"Bienvenido {username}"})
            else:
                return render(req, "login.html", {"formulario":formulario})
        else:
            return render(req, "login.html", {"formulario":formulario})
    else:
        formulario = AuthenticationForm()
        return render(req, "login.html", {"formulario": formulario})

def register(req: HttpRequest):
    if req.method == 'POST':
        formulario = UserRegisterForm(req.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            username = data['username']
            formulario.save()
            return render(req, "register_success.html", {"message": f"Usuario {username} creado con exito!"})
#        else:
            # return render(req, "register.html", {"formulario": formulario})
    else:
        formulario = UserRegisterForm()
    return render(req, "register.html", {"formulario": formulario})

@login_required
def edit_perfil(req: HttpRequest):

    user = req.user

    if req.method == 'POST':
        formulario = UserEditForm(req.POST, instance=req.user )
    
        if formulario.is_valid():

            data = formulario.cleaned_data

            user.first_name = data['first_name']
            user.last_name = data['last_name']
            # user.email = data['email']
            user.set_password(data["password1"])
            user.save()
            return render(req, "dashboard.html", {"message": "Perfil actualizado con exito"})
        else:
            return render(req, 'edit_perfil.html', {"formulario": formulario})
    else:
        formulario = UserEditForm(instance=req.user)    
    
        return render(req, 'edit_perfil.html', {"formulario": formulario})

@login_required
def add_avatar(req: HttpRequest):
    if req.method == 'POST':
        formulario = AvatarForm(req.POST, req.FILES)
        if formulario.is_valid():

            data = formulario.cleaned_data

            avatar = Avatar(user=req.user, image=data['image'])

            avatar.save()

            return render(req, "dashboard.html", {"message": f"Avatar actualizado con exito!"})

        else:
            return render(req, "dashboard.html", {"message": "Formulario invalido"})
        
    else:
        formulario = AvatarForm()
        return render(req, "add_avatar.html", {"formulario": formulario})

@login_required
def edit_avatar(request):
    user = request.user
    try:
        avatar = Avatar.objects.get(user=user)
    except Avatar.DoesNotExist:
        avatar = None

    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            if avatar:
                avatar.image = form.cleaned_data['image']
            else:
                avatar = Avatar(user=user, image=form.cleaned_data['image'])
            avatar.save()
            return redirect('EditAvatar') 

    else:
        form = AvatarForm(instance=avatar)

    return render(request, 'edit_avatar.html', {'form': form, 'avatar': avatar})


@login_required
def conversation_list(request: HttpRequest):
    conversations = request.user.conversations.all()
    return render(request, 'conversation_list.html', {'conversations': conversations})

@login_required
def conversation_detail(request, conversation_id):
    conversation = Conversation.objects.get(pk=conversation_id)
    messages = Message.objects.filter(conversation=conversation).order_by('timestamp')
    
    if request.method == 'POST':
        text = request.POST.get('message_text')
        sender = request.user
        message = Message(text=text, sender=sender, conversation=conversation)
        message.save()

    return render(request, 'conversation_detail.html', {'conversation': conversation, 'messages': messages})


@login_required
def enviar_mensaje(request):
    if request.method == 'POST':
        recipient_id = request.POST.get('recipient')
        message_text = request.POST.get('message_text')

        # Obtener el destinatario y el remitente
        recipient = User.objects.get(pk=recipient_id)
        sender = request.user

        # Crear una nueva conversación
        conversation = Conversation.objects.create()
        conversation.participants.add(sender, recipient)

        # Crear el mensaje inicial
        message = Message.objects.create(
            text=message_text,
            sender=sender,
            conversation=conversation
        )

        # Redirigir a la página de detalle de la conversación recién creada
        return redirect('conversation_detail', conversation_id=conversation.id)

    # Obtener la lista de usuarios (puedes personalizar esto según tus necesidades)
    users = User.objects.all()

    return render(request, 'enviar_mensaje.html', {'users': users})

@login_required
def help(req):
    return render(req,'help.html')

def update_comment_state(request, comment_id, comment_state):
    try:
        comment = TasksListRows.objects.get(pk=comment_id)
        comment.state = comment_state
        comment.save()
        return JsonResponse({'success': True})
    except TasksListRows.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Comentario no encontrado'})


from django.shortcuts import render

def error_404_view(req, exception):
    return render(req, '404.html', status=404)
