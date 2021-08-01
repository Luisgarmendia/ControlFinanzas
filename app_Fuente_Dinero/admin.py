from django.contrib import admin
#importamos modelos
from app_Fuente_Dinero.models import *


#forma bonita de mostrar los modelos en el admin
class Admin_Fuente_Dinero(admin.ModelAdmin):   
    list_display = ('id','Fecha_Registro','Fuente','Saldo')
    list_filter = ('Fecha_Registro',)
    search_fields = ('Fuente',)
    date_hierarchy = 'Fecha_Registro'   




# Register your models here.
admin.site.register(FuenteDinero,Admin_Fuente_Dinero) 