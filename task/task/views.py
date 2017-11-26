from django.shortcuts import render
from django import forms
from django.db.models import Q
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.views.generic import TemplateView
from django.template.context import RequestContext

from .models import Task
from .models import Uploads
from .forms import TaskCreate
from .forms import UploadCreate
from .settings import MEDIA_ROOT

def mainlogout(request):
    logout(request)
    return redirect('/')

def home(request):

    template = 'base.html'

    title = "Log in with you Google Account!"
    tasks = None
    if request.user.is_authenticated():
        tasks = Task.objects.all()

    taskForm = TaskCreate()
    uploadForm = UploadCreate()

    if "create_task" in request.POST:
        taskForm = TaskCreate(request.POST, request.FILES)
        uploadForm = UploadCreate(request.POST, request.FILES)
        if taskForm.is_valid():
            newTask = taskForm.save(commit=False)
            newTask.owner = request.user.email
            newTask.save()
            idAux = Task.objects.all().order_by("-id")[0].id
            if request.FILES:
                files = request.FILES.getlist('attached')
                for f in files:
                    uploadAux = Uploads(uploaded_by_id=idAux, attached = f)
                    uploadAux.save()
        return redirect('/')
    elif "delete_task" in request.POST:
        Task.objects.filter(id=int(request.POST.get('id', ''))).delete()
        return redirect('/')
    elif "state_task" in request.POST:
        update = Task.objects.get(id=int(request.POST.get('id', '')))
        if update:
            if update.state:
                update.state = False
                update.updated_by = None
            else:
                update.state = True
                update.updated_by = request.user.email
            update.save()
        return redirect('/')

    context = {
        'template_create_task_form' : taskForm,
        'template_create_upload_form': uploadForm,
        'tasks' : tasks,
        'title' : title,
        'uploadPath' : MEDIA_ROOT,
        'is_authenticated' : request.user.is_authenticated(),
        'request': request,
        'user': request.user,
    }

    return render(request, 'base.html', context)
