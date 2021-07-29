#crear urls Fuente Dinero
from django.urls import path
from . import views

app_name = 'FuenteDinero'

urlpatterns = [
    path('',views.index ,name='index'),
    path('create/',views.create, name='create'),
    path('edit/<int:id>',views.edit , name='edit'),
    path('delete/<int:id>',views.delete , name='delete'),
]