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
        if idFuente:
            fuente = FuenteDinero.objects.get(id=idFuente)
            if monto > 0:
                if fuente.Saldo > monto :
                    fuente.Saldo = fuente.Saldo - monto
                    fuente.save()
                    p = Gasto(Fuente=fuente,Fecha_Registro=hoy,Tipo=tipoGasto, Monto=monto)
                    p.save()
                    messages.add_message(request, messages.ERROR, 'Se ha registrado su gasto.')
                else:
                    messages.add_message(request, messages.ERROR, 'El monto es insuficiente.')
            else:
                messages.add_message(request, messages.ERROR, 'Ingrese un monto mayor a 0.')
            
            return redirect(reverse('Gastos:index'))
        else:
            messages.add_message(request, messages.ERROR, 'Debe seleccionar una fuente')
        
    data = Gasto.objects.filter(Fuente__Cliente__Usuario=request.user)
    ctx = {
        'Gasto': data,
        'TipoGasto': data2,
        'Fuente': data3,
    }
    return render(request, 'gastos/index.html',ctx)

def actualizar_gasto(request, id):
    gasto = Gasto.objects.get(pk=id)
    data = Gasto.objects.filter(Fuente__Cliente__Usuario=request.user)
    data2 = TipoGasto.objects.all()
    data3 = FuenteDinero.objects.filter(Cliente__Usuario=request.user)

    fuente_antigua = gasto.Fuente
    monto_antiguo = gasto.Monto

    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        monto = int(request.POST.get('monto'))
        idFuente = request.POST.get('fuente')
        tipoGasto = TipoGasto.objects.get(id=tipo)
        fuente = FuenteDinero.objects.get(id=idFuente)


        if monto > 0:
            if fuente == gasto.Fuente:
                if monto > monto_antiguo and fuente.Saldo > monto:
                    fuente.Saldo -= monto - monto_antiguo
                    fuente.save()
                    gasto.Fuente = fuente
                    gasto.Tipo = tipoGasto
                    gasto.Monto = monto
                    gasto.save()
                    messages.add_message(request, messages.ERROR, 'Su gasto se ha actualizado.')
                elif monto < monto_antiguo and fuente.Saldo > monto:
                    fuente.Saldo += monto_antiguo - monto
                    fuente.save()
                    gasto.Fuente = fuente
                    gasto.Tipo = tipoGasto
                    gasto.Monto = monto
                    gasto.save()
                    messages.add_message(request, messages.ERROR, 'Su gasto se ha actualizado.')
                elif monto == monto_antiguo:
                    gasto.Fuente = fuente
                    gasto.Tipo = tipoGasto
                    gasto.Monto = monto
                    gasto.save()
                    messages.add_message(request, messages.ERROR, 'Su gasto se ha actualizado.')
                else:
                    messages.add_message(request, messages.ERROR, 'El monto es insuficiente.')   
            elif fuente != gasto.Fuente:
                if fuente.Saldo > monto:
                    fuente_antigua.Saldo += monto_antiguo
                    fuente.Saldo -= monto
                    fuente_antigua.save()
                    fuente.save()
                    gasto.Fuente = fuente
                    gasto.Tipo = tipoGasto
                    gasto.Monto = monto
                    gasto.save()
                    messages.add_message(request, messages.ERROR, 'Su gasto se ha actualizado.')
                else:
                    messages.add_message(request, messages.ERROR, 'El monto es insuficiente')
            else:
                messages.add_message(request, messages.ERROR, 'Error desconocido')
        else:
            messages.add_message(request, messages.ERROR, 'Ingrese un monto mayor a 0.')

        return redirect(reverse('Gastos:index'))
    else:
        ctx = {
            'Gasto': data,
            'TipoGasto': data2,
            'Fuente': data3,
            'GastoActual': gasto,
        }
    
    
        return render(request, 'Gastos/index.html', ctx)

def eliminar_gasto(request, id,idFuente, monto):
    Gasto.objects.get(pk=id).delete()
    montoRecuperado = monto
    fuente = FuenteDinero.objects.get(id=idFuente)
    fuente.Saldo = fuente.Saldo + montoRecuperado
    fuente.save()
    return redirect(reverse('Gastos:index'))