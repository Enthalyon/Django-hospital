from rest_framework import serializers
from pacienteApp.models.paciente import Paciente

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['id', 'id_profesional_medico', 'id_familiar_asignado', 'id_usuario', 'nombres', 'apellidos', 'telefono', 'genero', 'direccion', 'ciudad', 'fecha_de_nacimiento']