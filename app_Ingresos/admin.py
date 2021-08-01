from django.contrib import admin
#importamos models
from app_Ingresos.models import *


#forma bonita de mostrar los modelos en el admin
class Admin_Ingresos(admin.ModelAdmin):   
    list_display = ('id','Fecha_Registro','Fuente','Monto')
    list_filter = ('Fecha_Registro',)
    search_fields = ('Fuente',)
    date_hierarchy = 'Fecha_Registro'

# Register your models here.
admin.site.register(Ingreso,Admin_Ingresos) 