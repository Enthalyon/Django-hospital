from django.db import models
from usuariosApp.models.usuario import Usuario

class FamiliarAsignado(models.Model):
    id_usuario = models.ForeignKey(Usuario, null=False ,on_delete=models.CASCADE, unique=True)
    nombres = models.CharField('Nombre', max_length=50, null=False, default="Sin nombre")
    apellidos = models.CharField('Apellido', max_length=50, null=False, default="Sin apellido")
    telefono = models.CharField('Telefono', max_length=50, null=False, default="Sin telefono")
    genero = models.CharField('Genero', max_length=50, null=False, default='Sin genero')
    direccion = models.CharField('Direccion', max_length=50, null=False, default="Sin direccion")
    parentesco = models.CharField('Parentesco', max_length=50, null=False, default='Sin parentesco')
