from django.db import models

class FuenteDinero(models.Model):
    Cliente = models.ForeignKey('app_Clientes.Cliente', verbose_name=("Cliente"), on_delete=models.CASCADE)
    Fecha_Registroc = models.DateField()
    Fuente = models.CharField(max_length=25)
    Saldo = models.IntegerField()
    class Meta:
        verbose_name = ("Fuente de Dinero")
        verbose_name_plural =("Fuente de Dinero")

    def __str__(self):
        return f"Cliente: {self.Cliente}"
# Create your models here.
