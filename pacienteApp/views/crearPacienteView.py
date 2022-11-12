from rest_framework.response import Response
from rest_framework import generics, status, authentication
from rest_framework.permissions import IsAuthenticated

from pacienteApp.models import Paciente
from pacienteApp.serializers import PacienteSerializer

class CrearPacienteView(generics.RetrieveAPIView):
    authentication_classes = [authentication.TokenAuthentication]

    def post(self, request, *args, **kwargs):
        serializer = PacienteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)