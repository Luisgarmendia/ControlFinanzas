
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from app_Clientes.models import Cliente
from django.contrib.auth.models import User

def index(request):
    if request.user.is_authenticated:
        return redirect(reverse('Clientes:index'))

    return render(request, 'login/index.html')

def registro_cliente(request):
    err = False
    if request.method =='POST':
        name = request.POST.get('nombre')
        lastname = request.POST.get('apellido')
        username = request.POST.get('usuario')
        password = request.POST.get('contrasena')
        confpass = request.POST.get('confirmcontrasena')

        usr_exist =  User.objects.filter(username=username).count()

        if password != confpass:
            err=True
            messages.add_message(request, messages.INFO, 'Confirma la contraña')
        if usr_exist > 0:
            err=True
            messages.add_message(request, messages.INFO, 'Este usuario ya existe')
        if not err:
            newuser = User.objects.create_user(username=username,password=password)
            newuser.save()
            cliente = Cliente(Nombre=name,Apellido=lastname,Usuario=newuser)
            cliente.save()
            return(render(request,'login/index.html'))
        else:
            return(render(request,'login/registro.html'))

    else:
        return(render(request,'login/registro.html'))

def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('usuario')
        password = request.POST.get('contrasena')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(reverse('Clientes:index'))
        else:
            messages.add_message(request, messages.ERROR, 'El usuario/contraseña inválidos o la cuenta está desactivada')
            return redirect('/')

    else:
        return redirect('/')


def log_out(request):
    logout(request)
    return redirect('/')