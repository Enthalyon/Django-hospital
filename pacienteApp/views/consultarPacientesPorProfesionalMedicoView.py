from rest_framework.response import Response
from rest_framework import generics, status, authentication

from pacienteApp.models import Paciente
from pacienteApp.serializers import PacienteSerializer

class ConsultarPacientesPorProfesionalMedicoView(generics.RetrieveAPIView):
    authentication_classes = [authentication.TokenAuthentication]

    def get(self, request, *args, **kwargs):
        try:
            modelo_vista = Paciente.objects.filter(id_profesional_medico=kwargs['pk'])
        except Paciente.DoesNotExist:
            return Response(
                {'El usuario asignado con este id no existe'},
                status = status.HTTP_400_BAD_REQUEST
            )
        serializer = PacienteSerializer(modelo_vista,many=True)
        print(serializer.data)
        return Response (serializer.data, status=status.HTTP_200_OK)