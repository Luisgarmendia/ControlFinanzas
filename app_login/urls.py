#crear urls logeo
from django.urls import path
from . import views

app_name = 'app_login'

urlpatterns = [
    path('',views.index),
    path('registro/',views.registro_cliente,name="registro_cliente"),#URL DE REGISTRO DE USUARIOS DE LA APLICACION LOGIN
    path('login/',views.log_in,name='login_view'),#URL LOGIN
    path('logout/',views.log_out,name='logout_view'),#URL LOGOUT
]
