##SE AGREGO ESTE ARCHIVO PARA GUARDAR LAS DIRECCIONES PROPIAS DE GASTOS


from django.urls import path
from . import views

app_name = 'Gastos'

urlpatterns = [
    path('', views.index, name='index'),
    path('registrar/', views.registrar_gasto, name="registrar_gasto"),
    path('registrar/<int:id>/<int:idFuente>/<int:monto>/eliminar/', views.eliminar_gasto, name='eliminar_gasto'),
]