from django.contrib import admin
from app_Gastos.models import *
# Register your models here.

class GastosAdmin(admin.ModelAdmin):
    list_display = ('id','Fecha_Registro','Tipo','Monto')
    list_filter = ('Fecha_Registro',)
    search_fields = ('Monto',)
    date_hierarchy = 'Fecha_Registro' 

admin.site.register(TipoGasto)
admin.site.register(Gasto,GastosAdmin)
