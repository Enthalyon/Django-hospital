from rest_framework import serializers
from profesionalApp.models.profesionalMedico import ProfesionalMedico

class ProfesionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfesionalMedico
        fields = ['id', 'id_usuario', 'nombres', 'apellidos', 'telefono', 'genero', 'direccion', 'especialidad', 'es_medico']