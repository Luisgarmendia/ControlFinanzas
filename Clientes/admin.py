from django.contrib import admin
from .models import Cliente, FuenteDinero, TipoGasto, Gasto, Ingreso
# Register your models here.
admin.site.register(Cliente)
admin.site.register(FuenteDinero)
admin.site.register(Ingreso)
admin.site.register(Gasto)
admin.site.register(TipoGasto)