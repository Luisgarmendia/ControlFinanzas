from django.shortcuts import render
from .models import Cliente
# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def clientes(request):    
    #bucar los datos de la base de datos de Clientes
    # y pasarlos a la plantilla para mostrarlos en pantalla
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes}) 


