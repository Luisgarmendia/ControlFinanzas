#crear path de la app_Ingresos
from django.urls import path

from . import views

#nombre de la app: app_Ingresos
app_name = 'Ingresos'


urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='about'),
]




