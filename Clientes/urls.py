##SE AGREGO ESTE ARCHIVO PARA GUARDAR LAS DIRECCIONES PROPIAS DE CLIENTES


from django.urls import path
from . import views

app_name = 'Clientes'

urlpatterns = [
    path('', views.index, name='index'),
]