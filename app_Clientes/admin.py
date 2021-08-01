from django.contrib import admin
#imports do modelo
from .models import Cliente
# Register your models here.


#forma bonita de mostrar los modelos en el admin
class Admin_Clientes(admin.ModelAdmin):   
    list_display = ('id','Nombre','Apellido')
    search_fields = ('Nombre',)

app_name = 'Clientes'


admin.site.register(Cliente, Admin_Clientes)
