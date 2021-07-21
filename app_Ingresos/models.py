from django.db import models

# Create your models here.
class Ingreso(models.Model):   
    Fuente = models.ForeignKey('app_Fuente_Dinero.FuenteDinero',verbose_name=("Fuente") , on_delete=models.CASCADE, null=True, blank=True)
    Fecha_Registro = models.DateField()
    Monto= models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    class Meta: verbose_name_plural = ("Ingresos")
    def __str__(self): 
        return f"{self.Monto}"