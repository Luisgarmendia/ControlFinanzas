from django.shortcuts import render
from app_Clientes.models import Cliente
from app_Fuente_Dinero.models import FuenteDinero
from app_Gastos.models import Gasto, TipoGasto
from app_Ingresos.models import Ingreso
from django.db.models import Sum
from datetime import datetime
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    labels = []
    data = []
    labels2 = []
    data2 = []
    filtro = 0
    busqueda = 0
    mesActual = datetime.now().month
    Saldo = FuenteDinero.objects.filter(Cliente = request.user.cliente).aggregate(t=Sum('Saldo'))['t']
    Saldo = Saldo if Saldo else 0

    data3 = Ingreso.objects.filter(Fuente__Cliente__Usuario=request.user, Fecha_Registro__month=mesActual)
    data4 = Gasto.objects.filter(Fuente__Cliente__Usuario=request.user, Fecha_Registro__month=mesActual)
    queryset = Gasto.objects.filter(Fuente__Cliente__Usuario=request.user,Fecha_Registro__month=mesActual).values('Tipo').order_by('Tipo').annotate(montoTipo=Sum('Monto'))
    queryset2 = Ingreso.objects.filter(Fuente__Cliente__Usuario=request.user,Fecha_Registro__month=mesActual).values('Fuente').order_by('Fuente').annotate(montoFuente=Sum('Monto'))
    for gasto in queryset:
        tipo = TipoGasto.objects.get(id=gasto.get('Tipo'))
        labels.append(tipo.Tipo)
        data.append(gasto.get('montoTipo'))
    
    for ingreso in queryset2:
        fuente = FuenteDinero.objects.get(id=ingreso.get('Fuente'))
        labels2.append(fuente.Fuente)
        data2.append(ingreso.get('montoFuente'))

    if request.method == 'POST':
        labels = []
        data = []
        labels2 = []
        data2 = []
        filtro = request.POST.get('tipos')
        if filtro == '1':
            inicio = request.POST.get('inicio')
            if not inicio:
                inicio = str(datetime.now())
            
            busqueda = request.POST.get('busqueda')
            datosFecha = inicio.split("-")
            mesInicio = datosFecha[1]
            anioInicio = datosFecha[0]
            if busqueda == '1':
                queryset = Gasto.objects.filter(Fuente__Cliente__Usuario=request.user,Fecha_Registro__month=mesInicio,Fecha_Registro__year=anioInicio).values('Tipo').order_by('Tipo').annotate(montoTipo=Sum('Monto'))
                data4 = Gasto.objects.filter(Fuente__Cliente__Usuario=request.user, Fecha_Registro__month=mesInicio,Fecha_Registro__year=anioInicio)
                for gasto in queryset:
                    tipo = TipoGasto.objects.get(id=gasto.get('Tipo'))
                    labels.append(tipo.Tipo)
                    data.append(gasto.get('montoTipo'))
            elif busqueda == '2':
                queryset = Gasto.objects.filter(Fuente__Cliente__Usuario=request.user,Fecha_Registro__year=anioInicio).values('Tipo').order_by('Tipo').annotate(montoTipo=Sum('Monto'))
                data4 = Gasto.objects.filter(Fuente__Cliente__Usuario=request.user,Fecha_Registro__year=anioInicio)
                for gasto in queryset:
                    tipo = TipoGasto.objects.get(id=gasto.get('Tipo'))
                    labels.append(tipo.Tipo)
                    data.append(gasto.get('montoTipo'))
            else:
                print("no hay nada")
            
        elif filtro == '2':
            inicio = request.POST.get('inicio')
            if not inicio:
                inicio = str(datetime.now())
            busqueda = request.POST.get('busqueda')
            datosFecha = inicio.split("-")
            mesInicio = datosFecha[1]
            anioInicio = datosFecha[0]
            if busqueda == '1':
                queryset2 = Ingreso.objects.filter(Fuente__Cliente__Usuario=request.user,Fecha_Registro__month=mesInicio,Fecha_Registro__year=anioInicio).values('Fuente').order_by('Fuente').annotate(montoFuente=Sum('Monto'))
                data3 = Ingreso.objects.filter(Fuente__Cliente__Usuario=request.user, Fecha_Registro__month=mesInicio,Fecha_Registro__year=anioInicio)
                for ingreso in queryset2:
                    fuente = FuenteDinero.objects.get(id=ingreso.get('Fuente'))
                    labels.append(fuente.Fuente)
                    data.append(ingreso.get('montoFuente'))
            elif busqueda == '2':
                queryset2 = Ingreso.objects.filter(Fuente__Cliente__Usuario=request.user,Fecha_Registro__year=anioInicio).values('Fuente').order_by('Fuente').annotate(montoFuente=Sum('Monto'))
                data3 = Ingreso.objects.filter(Fuente__Cliente__Usuario=request.user, Fecha_Registro__year=anioInicio)
                for ingreso in queryset2:
                    fuente = FuenteDinero.objects.get(id=ingreso.get('Fuente'))
                    labels.append(fuente.Fuente)
                    data.append(ingreso.get('montoFuente'))
            else:
                print("no hay nada")

        elif filtro == '3':
            inicio = request.POST.get('inicio')
            if not inicio:
                inicio = str(datetime.now())
            busqueda = request.POST.get('busqueda')
            datosFecha = inicio.split("-")
            mesInicio = datosFecha[1]
            anioInicio = datosFecha[0]
            if busqueda == '1':
                queryset = Gasto.objects.filter(Fuente__Cliente__Usuario=request.user,Fecha_Registro__month=mesInicio,Fecha_Registro__year=anioInicio).values('Tipo').order_by('Tipo').annotate(montoTipo=Sum('Monto'))
                data4 = Gasto.objects.filter(Fuente__Cliente__Usuario=request.user, Fecha_Registro__month=mesInicio,Fecha_Registro__year=anioInicio)
                queryset2 = Ingreso.objects.filter(Fuente__Cliente__Usuario=request.user,Fecha_Registro__month=mesInicio,Fecha_Registro__year=anioInicio).values('Fuente').order_by('Fuente').annotate(montoFuente=Sum('Monto'))
                data3 = Ingreso.objects.filter(Fuente__Cliente__Usuario=request.user, Fecha_Registro__month=mesInicio,Fecha_Registro__year=anioInicio)
                for gasto in queryset:
                    tipo = TipoGasto.objects.get(id=gasto.get('Tipo'))
                    labels.append(tipo.Tipo)
                    data.append(gasto.get('montoTipo'))
                for ingreso in queryset2:
                    fuente = FuenteDinero.objects.get(id=ingreso.get('Fuente'))
                    labels2.append(fuente.Fuente)
                    data2.append(ingreso.get('montoFuente'))
            elif busqueda == '2':
                queryset = Gasto.objects.filter(Fuente__Cliente__Usuario=request.user,Fecha_Registro__year=anioInicio).values('Tipo').order_by('Tipo').annotate(montoTipo=Sum('Monto'))
                data4 = Gasto.objects.filter(Fuente__Cliente__Usuario=request.user,Fecha_Registro__year=anioInicio)
                queryset2 = Ingreso.objects.filter(Fuente__Cliente__Usuario=request.user,Fecha_Registro__year=anioInicio).values('Fuente').order_by('Fuente').annotate(montoFuente=Sum('Monto'))
                data3 = Ingreso.objects.filter(Fuente__Cliente__Usuario=request.user,Fecha_Registro__year=anioInicio)
                for gasto in queryset:
                    tipo = TipoGasto.objects.get(id=gasto.get('Tipo'))
                    labels.append(tipo.Tipo)
                    data.append(gasto.get('montoTipo'))
                for ingreso in queryset2:
                    fuente = FuenteDinero.objects.get(id=ingreso.get('Fuente'))
                    labels2.append(fuente.Fuente)
                    data2.append(ingreso.get('montoFuente'))
        elif filtro == '4':
            data3 = Ingreso.objects.filter(Fuente__Cliente__Usuario=request.user, Fecha_Registro__month=mesActual)
            data4 = Gasto.objects.filter(Fuente__Cliente__Usuario=request.user, Fecha_Registro__month=mesActual)
            queryset = Gasto.objects.filter(Fuente__Cliente__Usuario=request.user,Fecha_Registro__month=mesActual).values('Tipo').order_by('Tipo').annotate(montoTipo=Sum('Monto'))
            queryset2 = Ingreso.objects.filter(Fuente__Cliente__Usuario=request.user,Fecha_Registro__month=mesActual).values('Fuente').order_by('Fuente').annotate(montoFuente=Sum('Monto'))
            for gasto in queryset:
                tipo = TipoGasto.objects.get(id=gasto.get('Tipo'))
                labels.append(tipo.Tipo)
                data.append(gasto.get('montoTipo'))
            
            for ingreso in queryset2:
                fuente = FuenteDinero.objects.get(id=ingreso.get('Fuente'))
                labels2.append(fuente.Fuente)
                data2.append(ingreso.get('montoFuente'))
        else:
            print("Seleccion")

    ctx = {
        'labels': labels,
        'data': data,
        'labels2': labels2,
        'data2': data2,
        'Gasto':data4,
        'Ingreso':data3,
        'filtro':filtro,
        'busqueda':busqueda,
        'Saldo':Saldo
    }
    return render(request, 'estadisticas/index.html',ctx)