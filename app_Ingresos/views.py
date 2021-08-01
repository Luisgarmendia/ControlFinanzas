from django.shortcuts import render,redirect
from .models import Ingreso
from app_Fuente_Dinero.models import FuenteDinero
from datetime import datetime
from django.contrib import messages
from django.urls import reverse

# Create your views here.
def index(request):
    data = Ingreso.objects.filter(Fuente__Cliente__Usuario=request.user)
    data2 = FuenteDinero.objects.filter(Cliente__Usuario=request.user)
    ctx = {
        'Ingreso': data,
        'Fuente': data2,
    }
    return render(request, 'Ingresos/index.html', ctx)

def registrar_ingreso(request):
    data = Ingreso.objects.filter(Fuente__Cliente__Usuario=request.user)
    data2 = FuenteDinero.objects.filter(Cliente__Usuario=request.user)
    
    if request.method == 'POST':
        idFuente = request.POST.get('fuente')
        hoy = datetime.now().date()
        monto = int(request.POST.get('monto'))

        if idFuente:
            fuente = FuenteDinero.objects.get(id=idFuente)
            if monto > 0:
                fuente.Saldo = fuente.Saldo + monto
                fuente.save()
                p = Ingreso(Fuente=fuente,Fecha_Registro=hoy, Monto=monto)
                p.save()
                messages.add_message(request, messages.ERROR, 'Se ha registrado su ingreso.')
            else:
                messages.add_message(request, messages.ERROR, 'Ingrese un monto mayor a 0.')
            return redirect(reverse('Ingresos:index'))
        else:
            messages.add_message(request, messages.ERROR, 'Debe seleccionar una fuente')
        
        
        
    data = Ingreso.objects.filter(Fuente__Cliente__Usuario=request.user)
    ctx = {
        'Ingreso': data,
        'Fuente': data2,
    }
    return render(request, 'Ingresos/index.html',ctx)


def actualizar_ingreso(request, id):
    ingreso = Ingreso.objects.get(pk=id)
    data = Ingreso.objects.filter(Fuente__Cliente__Usuario=request.user)
    data2 = FuenteDinero.objects.filter(Cliente__Usuario=request.user)

    monto_antiguo = ingreso.Monto

    if request.method == 'POST':
        idFuente = request.POST.get('fuente')
        monto = int(request.POST.get('monto'))
        fuente = FuenteDinero.objects.get(id=idFuente)


        if monto > 0:
            if fuente == ingreso.Fuente:
                if monto > monto_antiguo and fuente.Saldo > monto:
                    fuente.Saldo += monto - monto_antiguo
                    fuente.save()
                    ingreso.Fuente = fuente
                    ingreso.Monto = monto
                    ingreso.save()
                    messages.add_message(request, messages.ERROR, 'Su gasto se ha actualizado.')
                elif monto < monto_antiguo and fuente.Saldo > monto:
                    fuente.Saldo -= monto_antiguo - monto
                    fuente.save()
                    ingreso.Fuente = fuente
                    ingreso.Monto = monto
                    ingreso.save()
                    messages.add_message(request, messages.ERROR, 'Su gasto se ha actualizado.')
                elif monto == monto_antiguo:
                    ingreso.Fuente = fuente
                    ingreso.Monto = monto
                    ingreso.save()
                    messages.add_message(request, messages.ERROR, 'Su gasto se ha actualizado.')
                else:
                    messages.add_message(request, messages.ERROR, 'El monto es insuficiente.')   
        else:
            messages.add_message(request, messages.ERROR, 'Ingrese un monto mayor a 0.')

        return redirect(reverse('Ingresos:index'))
    else:
        ctx = {
            'Ingreso': data,
            'Fuente': data2,
            'IngresoActual': ingreso,
        }
    
    
        return render(request, 'Ingresos/index.html', ctx)



def eliminar_ingreso(request, id,idFuente, monto):
    Ingreso.objects.get(pk=id).delete()
    montoRecuperado = monto
    fuente = FuenteDinero.objects.get(id=idFuente)
    fuente.Saldo = fuente.Saldo - montoRecuperado
    fuente.save()
    return redirect(reverse('Ingresos:index'))