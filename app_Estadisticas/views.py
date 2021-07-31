from django.shortcuts import render
from app_Clientes.models import Cliente
from app_Fuente_Dinero.models import FuenteDinero
from app_Gastos.models import Gasto, TipoGasto
from django.db.models import Sum

def index(request):

    labels = ['hola','hola2']
    data = [1,2]

    queryset = Gasto.objects.filter(Fuente__Cliente__Usuario=request.user).values('Tipo').order_by('Tipo').annotate(montoTipo=Sum('Monto'))
    print(queryset)
    
    #for tipo in queryset:
    #    labels.append(dict([tipo.Tipo]))
    #    data.append(tipo.montoTipo)

    ctx = {
        'labels': labels,
        'data': data,
    }
    return render(request, 'estadisticas/index.html',ctx)