from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import logout as django_logout
from .models import Task
import datetime
import uuid


# Create your views here.

def index(request):
    task_list = Task.objects/filter(Q(owner=user) | Q(collaborators=user))
    return render(request, 'tasks.html', {'user':user, 'task_list':task_list})
        
def submittask(request):
    # create a form instance and populate it with data from the request:
    current_user = request.user
    title = request.POST['title']
    description = request.POST['description']
    # collaborators = request.POST['collaborators']
    task = Task.objects.create_task(current_user, title, description)
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request, 'tasks.html')
    
def delete(request):
    task_id = request.POST['delete']
    task = Task.objects.get(id=task_id)
    task.delete()
    return HttpResponseRedirect ('/tasks/')
    
def markcomplete(request):
    task_id = task_id = request.POST['markcomplete']
    task = Task.objects.get(id=task_id)
    if task.markcomplete == False:
        task.complete = True
        task.save()
    else:
        task.markcomplete = Falsetask.save()
    return HttpResponseRedirect ('/tasks/') 
    
    