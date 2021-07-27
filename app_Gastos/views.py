from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from app_Clientes.models import Cliente
from app_Fuente_Dinero.models import FuenteDinero
from .models import Gasto, TipoGasto
from datetime import datetime
from django.contrib import messages
from django.urls import reverse

# Create your views here.

def index(request):
    data = Gasto.objects.filter(Fuente__Cliente__Usuario=request.user)
    data2 = TipoGasto.objects.all()
    data3 = FuenteDinero.objects.filter(Cliente__Usuario=request.user)
    ctx = {
        'Gasto': data,
        'TipoGasto': data2,
        'Fuente': data3,
    }
    return render(request, 'gastos/index.html',ctx)

def registrar_gasto(request):
    data = Gasto.objects.filter(Fuente__Cliente__Usuario=request.user)
    data2 = TipoGasto.objects.all()
    data3 = FuenteDinero.objects.filter(Cliente__Usuario=request.user)
    
    if request.method == 'POST':
        hoy = datetime.now().date()
        tipo = request.POST.get('tipo')
        monto = int(request.POST.get('monto'))
        idFuente = request.POST.get('fuente')
        tipoGasto = TipoGasto.objects.get(id=tipo)
        fuente = FuenteDinero.objects.get(id=idFuente)
        if fuente.Saldo > monto:
            fuente.Saldo = fuente.Saldo - monto
            fuente.save()
            p = Gasto(Fuente=fuente,Fecha_Registro=hoy,Tipo=tipoGasto, Monto=monto)
            p.save()
        else:
            messages.add_message(request, messages.ERROR, 'El saldo es insuficiente')
        
    data = Gasto.objects.filter(Fuente__Cliente__Usuario=request.user)
    ctx = {
        'Gasto': data,
        'TipoGasto': data2,
        'Fuente': data3,
    }
    return render(request, 'gastos/index.html',ctx)

def eliminar_gasto(request, id,idFuente, monto):
    Gasto.objects.get(pk=id).delete()
    montoRecuperado = monto
    fuente = FuenteDinero.objects.get(id=idFuente)
    fuente.Saldo = fuente.Saldo + montoRecuperado
    fuente.save()
    return redirect(reverse('Gastos:index'))