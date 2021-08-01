from django.shortcuts import render
from .models import Cliente
# Create your views here.
#importar login required para evitar acceso no autorizado
from django.contrib.auth.decorators import login_required

#Importacion temporales para visualización de data en combobox (borrar)
from django.db.models import Sum
from app_Fuente_Dinero.models import FuenteDinero 
    
@login_required
def clientes(request):    
    #Data temporal para visualización de data en combobox (borrar)
    Saldo = FuenteDinero.objects.filter(Cliente = request.user.cliente).aggregate(Sum('Saldo'))
    FuentesD = FuenteDinero.objects.filter(Cliente = request.user.cliente)
    ctx={
        "Saldo":Saldo.get('Saldo__sum'),
        "Fuentes":FuentesD,
    }
    return render(request, 'Clientes/index.html', ctx)


