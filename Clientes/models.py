from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Cliente(models.Model):
    Nombre  = models.CharField(max_length=25, blank=True, null=True)
    Apellido  = models.CharField(max_length=25, blank=True, null=True)
    Usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True) #SE AGREGO DEVELOP_2
    class Meta:
        verbose_name = ("Cliente")
        verbose_name_plural =("Clientes")

    def __str__(self):
        return f"{self.Nombre} {self.Apellido}"


class FuenteDinero(models.Model):
    Cliente = models.ForeignKey(Cliente, verbose_name=("Cliente"), on_delete=models.CASCADE)
    Fecha_Registroc = models.DateField()
    Fuente = models.CharField(max_length=25)
    Saldo = models.IntegerField()
    class Meta:
        verbose_name = ("Fuente de Dinero")
        verbose_name_plural =("Fuente de Dinero")

    def __str__(self):
        return f"Cliente: {self.Cliente}"

# crear clase tipo de gastos
class TipoGasto(models.Model):
    Tipo = models.CharField(max_length=25)
    class Meta: verbose_name_plural = ("TipoGasto")
    def __str__(self):        
        return f"{self.Tipo}"

#crear clase de ingresos
class Ingreso(models.Model):   
    Fuente = models.ForeignKey(FuenteDinero, verbose_name=("Fuente"), on_delete=models.CASCADE)    
    Fecha_Registro = models.DateField()
    Monto= models.IntegerField()
    class Meta: verbose_name_plural = ("Ingreso")
    def __str__(self): 
        return f"{self.Monto}"


# Create model gastos
class Gasto(models.Model):
    Fuente = models.ForeignKey(FuenteDinero, verbose_name=("Fuente"), on_delete=models.CASCADE)
    Fecha_Registro = models.DateField()
    Tipo = models.ForeignKey(TipoGasto, verbose_name=("Tipo"), on_delete=models.CASCADE)
    Monto = models.IntegerField()
    class Meta:verbose_name_plural = ("Gasto")       
    def __str__(self):
        return f"{self.Monto}"
