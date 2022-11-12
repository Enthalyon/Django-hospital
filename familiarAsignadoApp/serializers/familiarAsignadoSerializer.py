from dataclasses import field, fields
from rest_framework import serializers
from familiarAsignadoApp.models.familiarAsignado import FamiliarAsignado

class FamiliarAsignadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamiliarAsignado
        fields = ['id', 'id_usuario', 'nombres', 'apellidos', 'telefono', 'genero', 'direccion', 'parentesco'] 