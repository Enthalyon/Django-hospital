from django.db import models
from usuariosApp.models.usuario import Usuario

class Auxiliar(models.Model):
    id_usuario = models.ForeignKey(Usuario, null=False, on_delete=models.CASCADE, unique=True)
    nombre = models.CharField('Nombre', max_length=50, null=False, default="Sin nombre")
    apellido = models.CharField('Apellido', max_length=50, null=False, default="Sin apellido")
