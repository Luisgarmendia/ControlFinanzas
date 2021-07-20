from django.shortcuts import get_object_or_404, render
from app_Fuente_Dinero.models import FuenteDinero 

#IMPORTAR MODELO de fuente dinero


# Create your views here.

#crear la vista de index
def index(request):

    return render(request, 'app_Fuente_Dinero/index.html')

#crear la vista de edit
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
def delete(request,id):
    FuenteDinero.objects.get(pk=id).delete()
    return render(request, 'app_Fuente_Dinero/index.html')
