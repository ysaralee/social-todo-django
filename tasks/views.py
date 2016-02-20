from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
import datetime


# Create your views here.

def index(request):
    return render(request, 'tasks.html')
        
def submittask(request):
    # create a form instance and populate it with data from the request:
    # current_user = request.user
    # title = request.POST['title']
    # description = request.POST['description']
    # # collaborators = request.POST['collaborators']
    # task = Task.objects.create_task(current_user, title, description)
    # # check whether it's valid:
    # if task is not None:
    #     if form.is_valid():
    #         # process the data in form.cleaned_data as required
    #         # ...
    #         # redirect to a new URL:
    #         return render(request, 'tasks.html', {'form': form})
    #     else:
    #         return render(request, 'tasks.html', {'errors': "Error with tasks."})
    # else:
    #     return render(request, 'tasks.html', {'errors': "Please fill out all the categories necessary."})
    return HttpResponseRedirect('http://www.facebook.com')