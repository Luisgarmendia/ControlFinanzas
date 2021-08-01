#crear urls Fuente Dinero
from django.urls import path
from . import views

app_name = 'FuenteDinero'

urlpatterns = [
    path('',views.index,name="index"),
    path('registrar/',views.registrar, name='registrar'),
    path('editar/<int:id>',views.editar , name='editar'),
    path('eliminar/<int:id>',views.eliminar , name='eliminar'),

]