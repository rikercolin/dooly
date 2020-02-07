from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .models import ToDo

def index(request):
    if request.user.is_authenticated:
        currentuser = request.user.get_username()
        usertodos = ToDo.objects.filter(username=currentuser)
        if usertodos is not None:
            
            categories = set()
            test = repr(usertodos)

            for task in usertodos.all():
                categories.add(task.todo_category)

            
            ## Render for users with todos ##
            return render(
                request,
                'main/index.html',
                context = {
                    "todos":usertodos,
                    "categories":categories,
                }
            )
        else:
            ## Render for users to add todos ##
            return render(
                request,
                'main/index.html'
            )

    ## Default Render for non Users ##
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
