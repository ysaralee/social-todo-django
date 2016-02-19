from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as django_login
import datetime

# Create your views here.

def index(request):
    return render(request, "index.html")

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    user = authenticate(username=email, password=password)
    # if user is not None:
        # if user.is_active:
            # login(request, user)
            # Redirect to a success page.
            # return render(request, "tasks.html")
        # else:
            # Return a 'disabled account' error message
    # else:
        # return render(request, "index.html")

def logout(request):
    return render(request, "index.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['password-conf']
 
        u = User.objects.create_user
        # create a new user object with that data
        # u = User(name="", asdf....)
        login(request, u)
        # Task.query.filter(Task.completed == True).first()
        # Task.query.collaborators.contains(1)
        # redirect to dashboard
