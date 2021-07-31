from django.urls import path
from . import views

app_name = 'Estadisticas'

urlpatterns = [
    path('', views.index, name='index'),
]