from django.shortcuts import render
from .models import Cliente
# Create your views here.
#importar login required para evitar acceso no autorizado
from django.contrib.auth.decorators import login_required



@login_required
def index(request):
    return render(request, 'Clientes/index.html', {})
    
@login_required
def clientes(request):    
    #bucar los datos de la base de datos de Clientes
    # y pasarlos a la plantilla para mostrarlos en pantalla
    clientes = Cliente.objects.all()
    return render(request, 'Clientes/index.html', {'clientes': clientes}) 


