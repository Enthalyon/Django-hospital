from rest_framework.response import Response
from rest_framework import generics, status, authentication
from rest_framework.permissions import IsAuthenticated

from pacienteApp.models import Paciente
from pacienteApp.serializers import PacienteSerializer

class ConsultarPacientesView(generics.RetrieveAPIView):
    authentication_classes = [authentication.TokenAuthentication]

    def get(self, request, *args, **kwargs):
        modelo_vista = Paciente.objects.all()
        serializer = PacienteSerializer(modelo_vista,many=True)
        print(serializer.data)
        return Response (serializer.data, status=status.HTTP_200_OK)