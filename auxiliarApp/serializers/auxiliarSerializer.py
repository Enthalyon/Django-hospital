from rest_framework import serializers
from auxiliarApp.models.auxiliar import Auxiliar

class AuxiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auxiliar
        fields = ['id', 'id_usuario', 'nombre', 'apellido']
