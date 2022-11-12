from django.db import models
from usuariosApp.models.usuario import Usuario

class ProfesionalMedico(models.Model):
    id_usuario = models.ForeignKey(Usuario, null=False, on_delete=models.CASCADE, unique=True)
    nombres = models.CharField('Nombres', max_length=50, null=False, default="Sin nombres")
    apellidos = models.CharField('Apellidos', max_length=50, null=False, default="Sin apellidos")
    telefono = models.CharField('Telefono', max_length=50, null=False, default="Sin telefono")
    genero = models.CharField('Genero', max_length=50, null=False, default='Sin genero')
    direccion = models.CharField('Direccion', max_length=50, null=False, default="Sin direccion")
    especialidad = models.CharField('Especialidad', max_length=50, null=False, default='Sin especialidad')
    es_medico = models.BooleanField('EsMedico', default=False)