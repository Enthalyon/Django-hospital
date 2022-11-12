from rest_framework import serializers
from usuariosApp.models.usuario import Usuario

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'email']