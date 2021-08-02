from django.contrib import admin
from app_Gastos.models import *
# Register your models here.

class GastosAdmin(admin.ModelAdmin):
    list_display = ('id','Fecha_Registro','Tipo','Monto')
    list_filter = ('Fecha_Registro',)
    search_fields = ('Monto',)
    date_hierarchy = 'Fecha_Registro'

class TipoGastoAdmin(admin.ModelAdmin):
    list_display = ('id','Tipo')
    list_filter = ('Tipo',)

admin.site.register(TipoGasto,TipoGastoAdmin)
admin.site.register(Gasto,GastosAdmin)
