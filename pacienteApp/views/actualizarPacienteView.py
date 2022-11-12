from rest_framework.response import Response
from rest_framework import generics, status, authentication
from rest_framework.permissions import IsAuthenticated

from pacienteApp.models import Paciente
from pacienteApp.serializers import PacienteSerializer

class ActualizarPacienteView(generics.RetrieveAPIView):
    authentication_classes = [authentication.TokenAuthentication]

    def get_object(self, id):
        try:
            return Paciente.objects.get(id=id)
        except Paciente.DoesNotExist:
            return None
            
    def put (self, request, *args, **kwargs):
        paciente_instance = self.get_object(kwargs['pk'])
        if not paciente_instance:
            return Response(
                {'El paciente asignado con este id no existe.'},
                status = status.HTTP_400_BAD_REQUEST
            )
        serializer = PacienteSerializer(instance= paciente_instance, data= request.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
