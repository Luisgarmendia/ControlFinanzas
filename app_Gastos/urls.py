##SE AGREGO ESTE ARCHIVO PARA GUARDAR LAS DIRECCIONES PROPIAS DE GASTOS


from django.urls import path
from . import views

app_name = 'Gastos'

urlpatterns = [
    path('', views.index, name='index'),
    path('registrar/', views.registrar_gasto, name="registrar_gasto"),
    path('registrar/<int:id>/actualizar/', views.actualizar_gasto, name="actualizar_gasto"),
    path('registrar/<int:id>/<int:idFuente>/<int:monto>/eliminar/', views.eliminar_gasto, name='eliminar_gasto'),
    path('editTipoGasto/', views.editTipoGasto, name='editTipoGasto'),
    path('deleteTipoGasto/<int:id>/',views.deleteTipoGasto, name='deleteTipoGasto'),
    path('addTipoGasto/',views.addTipoGasto, name='addTipoGasto')
]