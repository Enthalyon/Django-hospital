from rest_framework.response import Response
from rest_framework import generics, status, authentication

from profesionalApp.models import ProfesionalMedico
from profesionalApp.serializers import ProfesionalSerializer

class ConsultarProfesionalesView(generics.RetrieveAPIView):
    authentication_classes = [authentication.TokenAuthentication]

    def get(self, request, *args, **kwargs):
        modelo_vista = ProfesionalMedico.objects.all()
        serializer = ProfesionalSerializer(modelo_vista,many=True)
        return Response (serializer.data, status=status.HTTP_200_OK)