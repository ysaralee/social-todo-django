from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth import logout as django_logout
import datetime

# Create your views here.

def index(request):
    return render(request, "index.html")

def login(request):
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(username=email, password=password)
    if user is not None:
        if user.is_active:
            django_login(request, user)
            # Redirect to a success page.
            return render(request, "tasks.html")
        else:
            # Return a 'Email/Password' error message
            return render(request, "index.html", {'errors':"The email/password combination is incorrect!"})
    else:
        return render(request, "index.html", {'errors':"The email/password combination is incorrect!"})

def logout(request):
    django_logout(request)
    return render(request, "index.html")

def register(request):
    username = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']
    confirm_password = request.POST['password-conf']
 
    u = User.objects.create_user (email, email, password)
    # create a new user object with that data
    u = authenticate(username=email, email=email, password=password)
    django_login(request, u)
    
    if u is not None: 
        if password != confirm_password:
            return render(request, "index.html", {'errors':"Password confirmation does not match password."})
        else:
            return render(request, "tasks.html")
    else:
        return render(request, "index.html", {'errors':"All the fields are not filled out!"})