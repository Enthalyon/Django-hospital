from email.policy import default
from enum import unique
from django.db import models
from usuariosApp.models.usuario import Usuario
from profesionalApp.models.profesionalMedico import ProfesionalMedico
from familiarAsignadoApp.models.familiarAsignado import FamiliarAsignado

class Paciente(models.Model):
    id_profesional_medico = models.ForeignKey(ProfesionalMedico, null=True, on_delete=models.CASCADE, default=None)
    id_familiar_asignado = models.ForeignKey(FamiliarAsignado, null=True, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, null=True, on_delete=models.CASCADE, unique=True)
    nombres = models.CharField('Nombre', max_length=50, null=False, default="Sin nombre")
    apellidos = models.CharField('Apellido', max_length=50, null=False, default="Sin apellido")
    telefono = models.CharField('Telefono', max_length=50, null=False, default="Sin telefono")
    genero = models.CharField('Genero', max_length=50, null=False, default="Sin genero")
    direccion = models.CharField('Direccion', max_length=50, null=False, default="Sin direccion")
    ciudad = models.CharField('Ciudad', max_length=50, null=False, default="Sin ciudad")
    fecha_de_nacimiento = models.DateTimeField('FechaDeNacimiento', null=False, default="Sin fecha de nacimiento")