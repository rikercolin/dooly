from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .models import ToDo
from .customforms import ToDoForm
import time

def index(request):
    if request.user.is_authenticated:
        currentuser = request.user.get_username()

        ## Creating/Editing todos
        if request.method == 'POST':
            form = ToDoForm(request.POST)

            data = {
                'username':currentuser,
                'label':form.data.get('label'),
                'category':form.data.get('category'),
                'details':form.data.get('details'),
            }

            form = ToDoForm(data)
            if form.is_valid():
                todo = form.save(commit=False)
                todo.save(todo)

                return redirect("main:index")
        else:
            form = ToDoForm()

        ## Displaying todos
        usertodos = ToDo.objects.filter(username=currentuser)
        if usertodos is not None:

            categories = set()

            for task in usertodos.all():
                categories.add(task.category)


            ## Todo Render ##
            return render(
                request,
                'main/index.html',
                context = {
                    "todos":usertodos,
                    "categories":categories,
                    "todoform":form,
                }
            )

    ## Default Render ##
    return render(
        request,
        'main/index.html'
    )

def logout_request(request):
    logout(request)
    return redirect("main:index")


def login_request(request):

    ## Form Handling ##
    if request.method == "POST":
        registerform = UserCreationForm(request.POST, prefix='register')
        if registerform.is_valid():
            user = registerform.save()
            username = registerform.cleaned_data.get('username')
            messages.success(request, f"New Account Created: {username}")
            login(request, user)
            return redirect("main:index")
    else:
        registerform = UserCreationForm(prefix='register')

    if request.method == "POST" and not registerform.is_valid():
        loginform = AuthenticationForm(data=request.POST, prefix='login')

        if loginform.is_valid():

            username = loginform.cleaned_data.get('username')
            password = loginform.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f"Your logged in as: {username}")
                return redirect("main:index")
            else:
                messages.error(request,"Bad Auth")
    else:
        loginform = AuthenticationForm(prefix='login')

    ## Page Handling ##
    return render(
        request,
        'main/login-register.html',
        context={
            "registerform":registerform,
            "loginform":loginform,
            }

    )
