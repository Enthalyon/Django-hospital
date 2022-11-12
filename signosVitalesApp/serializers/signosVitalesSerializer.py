from rest_framework import serializers
from signosVitalesApp.models.signosVitales import SignosVitales

class SignosVitalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignosVitales
        fields = ['id', 'id_paciente', 'oximetria', 'temperatura', 'frecuencia_respiratoria', 'glicemia', 'comentario_medico']