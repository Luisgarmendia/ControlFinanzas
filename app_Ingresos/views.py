from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app_Ingresos.models import Ingreso 
from app_Fuente_Dinero.models import FuenteDinero

# Create your views here.
#crear la vista de index
@login_required
def index(request):
    Fuentes = FuenteDinero.objects.filter(Cliente = request.user.cliente)
    Ingresos=[]
    for f in Fuentes:
        Ingresos += Ingreso.objects.filter(Fuente = f)
    ctx={
        "Fuentes":Fuentes,
        "Ingresos":Ingresos,
    }
    return render(request, 'app_Ingresos/index.html',ctx)

@login_required
def create(request):
    if request.method == 'POST':
        Fuente = FuenteDinero.objects.get(id=request.POST.get('Fuente'))
        Fecha =  request.POST.get('Fecha')
        Monto = request.POST.get('Monto')
        
        Fuente.Saldo = Fuente.Saldo + int(Monto)
        Fuente.save()
        IngresoD = Ingreso(Fuente=Fuente,Fecha_Registro=Fecha,Monto=Monto)
        IngresoD.save()
    Fuentes = FuenteDinero.objects.filter(Cliente = request.user.cliente)
    return redirect('/ingresos/')