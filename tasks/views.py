from django.shortcuts import render
from django.http import HttpResponse
from .forms import TaskForm
import datetime

# Create your views here.

def index(request):
# if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TaskForm(request.POST)
        owner = request.POST['owner']
        title = request.POST['title']
        description = request.POST['description']
        collaborators = request.POST['collaborators']
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')
    
    # if a GET (or any other method) we'll create a blank form
    else:
        form = TaskForm()
    
    return render(request, 'tasks.html', {'form': form})
    
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