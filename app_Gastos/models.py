from django.db import models

#importamos el modelo de usuario


# crear clase tipo de gastos
class TipoGasto(models.Model):
    Tipo = models.CharField(max_length=25)
    Cliente = models.ForeignKey('app_Clientes.Cliente', verbose_name=("Cliente"), on_delete=models.CASCADE , null=True, blank=True)
    class Meta: verbose_name_plural = ("Tipo Gastos")
    def __str__(self):        
        return f"{self.Tipo}"


# Create your models here.
class Gasto(models.Model):
    Fuente = models.ForeignKey('app_Fuente_Dinero.FuenteDinero',verbose_name=("Fuente") , on_delete=models.CASCADE, null=True, blank=True)
    Fecha_Registro = models.DateField()
    Tipo = models.ForeignKey(TipoGasto, verbose_name=("Tipo"), on_delete=models.CASCADE)
    Monto = models.IntegerField()
    class Meta:verbose_name_plural = ("Gastos")       
    def __str__(self):
        return f"{self.Monto}"
