
from django.shortcuts import get_object_or_404, render
from app_Fuente_Dinero.models import FuenteDinero 
from django.db.models import Sum
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
        Cliente = request.User.Cliente 
        Fecha = request.POST.get('Fecha')
        Fuente = request.POST.get('Fuente')
        Saldo = request.POST.get('Saldo')
        
        FuenteD.Cliente=Cliente
        FuenteD.Fecha_Registro=Fecha
        FuenteD.Fuente=Fuente
        FuenteD.Saldo=Saldo
        
        FuenteD.save()

    ctx={
        "Fuente":FuenteD
    }
    return render(request, 'app_Fuente_Dinero/index.html' , ctx)
#crear la vista de edit

@login_required
def create(request):
    if request.method == 'POST':
        Cliente = request.User.Cliente 
        Fecha = request.POST.get('Fecha')
        Fuente = request.POST.get('Fuente')
        Saldo = request.POST.get('Saldo')
        
        FuenteD = FuenteDinero(Cliente=Cliente,Fecha_Registro=Fecha,Fuente=Fuente,Saldo=Saldo)
        FuenteD.save()


    return render(request, 'app_Fuente_Dinero/index.html')


#crear vita de delete
@login_required
def delete(request,id):
    FuenteDinero.objects.get(pk=id).delete()
    return render(request, 'app_Fuente_Dinero/index.html')
