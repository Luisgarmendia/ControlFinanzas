from django.shortcuts import render
from .models import Cliente
# Create your views here.
#importar login required para evitar acceso no autorizado
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

@login_required
def index(request):
    return render(request, 'Clientes/index.html', {})
 
@login_required
def clientes(request):    
    #bucar los datos de la base de datos de Clientes
    # y pasarlos a la plantilla para mostrarlos en pantalla
    clientes = Cliente.objects.all()
    return render(request, 'Clientes/index.html', {'clientes': clientes}) 
    

@login_required
def adminCuenta(request):
    cliente = Cliente.objects.get(Usuario=request.user)
    usuario = User.objects.get(id = request.user.id)
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        nomusuario =  request.POST.get('usuario')
        contra = request.POST.get('contra')
        confcontra = request.POST.get('confirmar')
        
        if nombre and apellido and nomusuario:
            if contra and confcontra :
                if confcontra == contra:
                    usuario.set_password(contra)
                    messages.add_message(request, messages.ERROR, f'Se ha cambiado tu contraseña')
                else:
                    messages.add_message(request, messages.ERROR, f'Las contraseñas no concuerdan')

            #Actualizacion de datos
            usr_exist =  User.objects.exclude(username = request.user.username).filter(username=nomusuario)
            if not usr_exist:
                cliente.Nombre = nombre
                cliente.Apellido = apellido
                usuario.username = nomusuario
                usuario.save()
                cliente.save()
                messages.add_message(request, messages.ERROR, f'Se ha actualziado tu informacion {request.user.id}')
            else:
                messages.add_message(request, messages.ERROR, 'Error, ya existe cliente con este nombre de usuario')

        else:
            messages.add_message(request, messages.ERROR, 'Un campo esta vacio')
    # apellido = cliente.apellido
    # nombreUsuario = cliente.Usuario.username
    ctx = {
        'cliente':cliente
    }
    return render(request,'Clientes/cuenta.html',ctx)
