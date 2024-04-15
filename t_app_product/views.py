from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import ProductForm
from .models import Product
from django.contrib.auth.decorators import login_required

@login_required
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

@login_required
def product(request):
    products = Product.objects.filter(user=request.user)
    return render(request, 'product.html', {'products': products})

@login_required
def create_product(request):
    if request.method == 'GET':
        return render(request, 'create_product.html', {'form': ProductForm()})
    else:
        try:
            form = ProductForm(request.POST, request.FILES)
            new_product = form.save(commit=False)
            new_product.user = request.user
            new_product.save()
            return redirect('product')
        except ValueError:
            return render(request, 'create_product.html', {
                'form': ProductForm(),
                'error': 'Please provide valid data'
            })

@login_required
def product_detail(request, product_id):
    if request.method == 'GET':
        product = get_object_or_404(Product, pk=product_id, user=request.user)
        form = ProductForm(instance=product)
        return render(request, 'product_detail.html', {'product': product, 'form': form})
    else:
        try:
            product = get_object_or_404(Product, pk=product_id, user=request.user)
            form = ProductForm(request.POST, request.FILES, instance=product)
            form.save()
            return redirect('product')
        except ValueError:
            return render(request, 'product_detail.html', {'product': product, 'form': form, 'error': "Error updating product"})

@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id, user=request.user)
    if request.method == 'POST':
        product.delete()
        return redirect('product')

@login_required
def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {'form': AuthenticationForm()})
    else:
        username = request.POST['username']
        password = request.POST['password']

        # Verificar si el usuario y la contraseña coinciden con los valores específicos
        if username == 'wletona' and password == 'Karin2100':
            return redirect('signup')  # Redirigir a signup.html si las credenciales son correctas
        else:
            # Autenticar al usuario normalmente si las credenciales no son las específicas
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(
                    'product')  # Redirigir a la página de producto si el usuario es autenticado correctamente
            else:
                error_message = 'Username or password is incorrect'
                return render(request, 'signin.html', {'form': AuthenticationForm(), 'error': error_message})
