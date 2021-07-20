from django.shortcuts import render

#IMPORTAR MODELO de fuente dinero


# Create your views here.

#crear la vista de index
def index(request):

    return render(request, 'app_Fuente_Dinero/index.html')

#crear la vista de edit
def edit(request):

    return render(request, 'app_Fuente_Dinero/index.html')
#crear la vista de edit

def create(request):

    return render(request, 'app_Fuente_Dinero/index.html')


#crear vita de delete
def delete(request):
    return render(request, 'app_Fuente_Dinero/index.html')
