from django.urls import path
from . import views

app_name = 'Ingresos'

urlpatterns = [
    path('', views.index, name='index'),
    path('registrar/', views.registrar_ingreso, name="registrar_ingreso"),
    path('registrar/<int:id>/actualizar/', views.actualizar_ingreso, name="actualizar_ingreso"),
    path('registrar/<int:id>/<int:idFuente>/<int:monto>/eliminar/', views.eliminar_ingreso, name='eliminar_ingreso'),
]