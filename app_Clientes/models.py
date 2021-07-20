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

