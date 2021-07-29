
from django.shortcuts import get_object_or_404, render, redirect
from app_Fuente_Dinero.models import FuenteDinero 
from django.db.models import Sum
import datetime
#IMPORTAR MODELO de fuente dinero
#importar login required para evitar acceso no autorizado
from django.contrib.auth.decorators import login_required


# Create your views here.

#crear la vista de index
@login_required
def index(request):
    Saldo = 0
    Saldo = FuenteDinero.objects.filter(Cliente = request.user.cliente).aggregate(Sum('Saldo'))
    FuentesD = FuenteDinero.objects.filter(Cliente = request.user.cliente)
    ctx={
        "Saldo":Saldo.get('Saldo__sum'),
        "Fuentes":FuentesD,
    }
    return render(request, 'app_Fuente_Dinero/index.html',ctx)

#crear la vista de edit
@login_required
def edit(request,id):
    FuenteD = get_object_or_404(FuenteDinero, pk=id)

    if request.method == 'POST':
        Fuente = request.POST.get('Fuente')
        Saldo = request.POST.get('Saldo')
        
        FuenteD.Fuente=Fuente
        FuenteD.Saldo=Saldo
        FuenteD.save()
        return redirect('/FuenteDinero/')
    Fuentes = FuenteDinero.objects.filter(Cliente = request.user.cliente)
    ctx={
        "Fuentes":Fuentes,
        "f":FuenteD
    }
    return render(request, 'app_Fuente_Dinero/index.html',ctx)
#crear la vista de edit

@login_required
def create(request):
    if request.method == 'POST':
        Cliente = request.user.cliente 
        Fecha = datetime.datetime.now()
        Fuente = request.POST.get('Fuente')
        Saldo = request.POST.get('Saldo')
        
        FuenteD = FuenteDinero(Cliente=Cliente,Fecha_Registro=Fecha,Fuente=Fuente,Saldo=Saldo)
        FuenteD.save()

    return redirect('/FuenteDinero/')


#crear vita de delete
@login_required
def delete(request,id):
    FuenteDinero.objects.get(pk=id).delete()
    return redirect('/FuenteDinero/')
