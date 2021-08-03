from django.db.models.aggregates import Sum
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from app_Clientes.models import Cliente
from app_Fuente_Dinero.models import FuenteDinero
from .models import Gasto, TipoGasto
from datetime import datetime
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    data = Gasto.objects.filter(Fuente__Cliente__Usuario=request.user)
    data2 = TipoGasto.objects.filter(Cliente__Usuario=request.user)
    data3 = FuenteDinero.objects.filter(Cliente__Usuario=request.user)
    Saldo = FuenteDinero.objects.filter(Cliente = request.user.cliente).aggregate(t=Sum('Saldo'))['t']
    Saldo = Saldo if Saldo else 0
    TotalGastos = Gasto.objects.filter(Fuente__Cliente__Usuario=request.user).aggregate(t=Sum('Monto'))['t']
    TotalGastos=TotalGastos if TotalGastos else 0
    ctx = {
        'Gasto': data,
        'TipoGasto': data2,
        'Fuente': data3,
        'Saldo': Saldo,
        'TotalGastos': TotalGastos,
    }
    return render(request, 'gastos/index.html',ctx)

@login_required
def registrar_gasto(request):
    data = Gasto.objects.filter(Fuente__Cliente__Usuario=request.user)
    data2 = TipoGasto.objects.filter(Cliente__Usuario=request.user)
    data3 = FuenteDinero.objects.filter(Cliente__Usuario=request.user)
    Saldo = FuenteDinero.objects.filter(Cliente = request.user.cliente).aggregate(t=Sum('Saldo'))['t']
    Saldo = Saldo if Saldo else 0
    TotalGastos = Gasto.objects.filter(Fuente__Cliente__Usuario=request.user).aggregate(t=Sum('Monto'))['t']
    TotalGastos=TotalGastos if TotalGastos else 0
    
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
        'Saldo': Saldo,
        'TotalGastos': TotalGastos,
    }
    return render(request, 'gastos/index.html',ctx)

@login_required
def actualizar_gasto(request, id):
    gasto = Gasto.objects.get(pk=id)
    data = Gasto.objects.filter(Fuente__Cliente__Usuario=request.user)
    data2 = TipoGasto.objects.filter(Cliente=request.user.cliente)
    data3 = FuenteDinero.objects.filter(Cliente__Usuario=request.user)
    Saldo = FuenteDinero.objects.filter(Cliente = request.user.cliente).aggregate(t=Sum('Saldo'))['t']
    Saldo = Saldo if Saldo else 0
    fuente_antigua = gasto.Fuente
    monto_antiguo = gasto.Monto
    TotalGastos = Gasto.objects.filter(Fuente__Cliente__Usuario=request.user).aggregate(t=Sum('Monto'))['t']
    TotalGastos=TotalGastos if TotalGastos else 0
    
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
            'Saldo': Saldo,
            'TotalGastos': TotalGastos,
        }
    
    
        return render(request, 'gastos/index.html', ctx)

@login_required
def eliminar_gasto(request, id, idFuente, monto):
    Gasto.objects.get(pk=id).delete()
    montoRecuperado = monto
    fuente = FuenteDinero.objects.get(id=idFuente)
    fuente.Saldo = fuente.Saldo + montoRecuperado
    fuente.save()
    return redirect(reverse('Gastos:index'))

@login_required
def addTipoGasto(request):
    if request.method == 'POST':
        tipo = request.POST.get('tipo')

        TipoGastoD = TipoGasto(Tipo=tipo,Cliente=request.user.cliente)
        TipoGastoD.save()
    return redirect(reverse('Gastos:index'))

@login_required
def editTipoGasto(request):
    print(request.POST)
    if request.is_ajax()and request.method == 'POST':
        TipoGastoD= TipoGasto.objects.get(id=request.POST.get('id'))
        tipo = request.POST.get('tipo')
        TipoGastoD.Tipo = tipo
        TipoGastoD.save()
    return redirect(reverse('Gastos:index'))
@login_required 
def deleteTipoGasto(request,id):
    TipoGasto.objects.get(pk=id).delete()
    return redirect(reverse('Gastos:index'))
