from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == "GET":
        return render(request, "signup.html", {"form": UserCreationForm()})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                )
                user.save()
                login(request, user)
                return redirect('home')  # Redirigir a 'home' después del inicio de sesión
            except IntegrityError:
                return render(
                    request,
                    "signup.html",
                    {"form": UserCreationForm(), "error": "User already exists"},
                )
            
        else:
            return render(
                request,
                "signup.html",
                {"form": UserCreationForm(), "error": "Passwords do not match"},
            )

def product(request):
    return render(request, 'product.html')

def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render (request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    if user is None:
        return render (request, 'signin.html', {
            'form': AuthenticationForm,
            'error': 'Username or password is incorrect'
            })
    else:
        login(request, user)
        return redirect('product')
    