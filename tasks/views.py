from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import logout as django_logout
from .models import Task
from django.db.models import Q
from itertools import chain
import datetime
import uuid


# Create your views here.

def index(request):
    current_user = request.user
    owned = Task.objects.filter(owner=current_user)
    collaborating = Task.objects.filter(collaborators__username = current_user)
    task_list = list(chain(owned,collaborating))
    for task in task_list:
        if task.owner == current_user:
            task.isOwnedBy = True
        else:
            task.isOwnedBy = False
        
    return render(request, 'tasks.html', {'user':current_user, 'task_list':task_list})
        
def submittask(request):
    # create a form instance and populate it with data from the request:
    current_user = request.user
    title = request.POST['title']
    description = request.POST['description']
    collaborator1 = request.POST['collaborator1']
    collaborator2 = request.POST['collaborator2']
    collaborator3 = request.POST['collaborator3']
    task = Task.objects.create_task(current_user, title, description)
    if collaborator1:
        if User.objects.filter(username=collaborator1).exists():
            task.collaborators.add(User.objects.get(username = collaborator1))
        else:
            return HttpResponseRedirect('/')
    if collaborator2:
        if User.objects.filter(username=collaborator2).exists():
            task.collaborators.add(User.objects.get(username = collaborator2))
        else:
            return HttpResponseRedirect('/')
    if collaborator3:
        if User.objects.filter(username=collaborator3).exists():
            task.collaborators.add(User.objects.get(username = collaborator3))
        else:
            return HttpResponseRedirect('/')
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request, 'tasks.html')
    
def delete(request):
    task_id = request.POST['delete']
    task = Task.objects.get(id=task_id)
    task.delete()
    return HttpResponseRedirect ('/tasks/')
    
def markcomplete(request):
    task_id = request.POST['markcomplete']
    print task_id
    task = Task.objects.get(id=task_id)
    print task
    if task.markcomplete == False:
        print "poo1"
        task.markcomplete = True
        task.save()
    else:
        print "poo2"
        task.markcomplete = False
        task.save()
    return HttpResponseRedirect ('/tasks/') 
    
    