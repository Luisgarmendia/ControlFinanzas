from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render,redirect
from app_Fuente_Dinero.models import FuenteDinero 
from app_Clientes.models import Cliente
from datetime import datetime
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
#IMPORTAR MODELO de fuente dinero\
from django.db.models import Sum


# Create your views here.

#crear la vista de index
@login_required
def index(request):
    fuente =  FuenteDinero.objects.filter(Cliente=request.user.cliente)
    Saldo = FuenteDinero.objects.filter(Cliente = request.user.cliente).aggregate(t=Sum('Saldo')).get('t')
    Saldo = Saldo if Saldo else 0
    TotalGastos=0
    TotalGastos = FuenteDinero.objects.filter(Cliente__Usuario=request.user).aggregate(t=Sum('Saldo'))['t']
    TotalGastos = TotalGastos if TotalGastos else 0
    ctx = {
        "Saldo":Saldo,
        'fuentes':fuente,
        'TotalGastos':TotalGastos
    }
    return render(request, 'RegistroFuente/index.html',ctx)

#crear la vista de edit
@login_required
def editar(request,id):
    FuenteD = get_object_or_404(FuenteDinero, pk=id)
    cliente = Cliente.objects.get(Usuario = request.user)
    fuente =  FuenteDinero.objects.filter(Cliente=cliente)
    if request.method == 'POST':
        Fuente = request.POST.get('nombre')
        Saldo = int(request.POST.get('monto'))
        
        if Saldo > 0:
            FuenteD.Fuente=Fuente
            FuenteD.Saldo=Saldo
            FuenteD.save()
        else:
            messages.add_message(request, messages.ERROR, 'No se ha ingresado un monto correcto.')
        return redirect(reverse('FuenteDinero:index'))
    else:
        Saldo = FuenteDinero.objects.filter(Cliente = request.user.cliente).aggregate(t=Sum('Saldo')).get('t')
        Saldo = Saldo if Saldo else 0
        TotalGastos = FuenteDinero.objects.filter(Cliente__Usuario=request.user).aggregate(t=Sum('Saldo'))['t']
        TotalGastos = TotalGastos if TotalGastos else 0
        ctx={
            "FuenteActual":FuenteD,
            'fuentes':fuente,
            "Saldo":Saldo,
            'TotalGastos':TotalGastos
        }

        return render(request, 'RegistroFuente/index.html' , ctx)
#crear la vista de edit
@login_required
def registrar(request):
    if request.method == 'POST':
         
        cliente =  Cliente.objects.get(Usuario = request.user)
        Fecha = datetime.now().date()
        fuente = request.POST.get('nombre')
        saldo = int(request.POST.get('monto'))
        fuentes_exist =  FuenteDinero.objects.filter(Fuente = fuente,Cliente=request.user.cliente).count()

        if not fuentes_exist:
            if saldo > 0:
                FuenteD = FuenteDinero(Cliente=cliente,Fecha_Registro=Fecha,Fuente=fuente,Saldo=saldo)
                FuenteD.save()
            else:
                messages.add_message(request, messages.ERROR, 'No se ha ingresado un monto correcto.')
        else:
            messages.add_message(request, messages.ERROR, 'Ya existe una fuente con ese nombre.')

    return redirect(reverse('FuenteDinero:index'))


#crear vita de delete
@login_required
def eliminar(request,id):
    FuenteDinero.objects.get(pk=id).delete()
    return redirect(reverse('FuenteDinero:index'))
