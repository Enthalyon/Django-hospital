from django.db import models
from pacienteApp.models.paciente import Paciente

class SignosVitales(models.Model):
    id_paciente = models.ForeignKey(Paciente, null=False, on_delete=models.CASCADE)
    oximetria = models.FloatField('Oximetria', null=True, default=0)
    temperatura = models.FloatField('Temperatura', null=True, default=0)
    frecuencia_respiratoria = models.FloatField('FrecuenciaRespiratoria', null=True, default=0)
    glicemia = models.FloatField('Glicemia', null=True, default=0)
    comentario_medico = models.CharField('ComentarioMedico', max_length=2000, null=True, default="Sin comentario medico")
