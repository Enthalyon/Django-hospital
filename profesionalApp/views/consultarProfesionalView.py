from rest_framework.response import Response
from rest_framework import generics, status, authentication

from profesionalApp.models import ProfesionalMedico
from profesionalApp.serializers import ProfesionalSerializer

class ConsultarProfesionalView(generics.RetrieveAPIView):
    authentication_classes = [authentication.TokenAuthentication]

    def get(self, request, *args, **kwargs):
        modelo_vista = ProfesionalMedico.objects.get(id_usuario=kwargs['pk'])
        if not modelo_vista:
            return Response(
                {"res":"El profesional con este id no existen"},
                status=status.HTTP_400_BAD_REQUEST
            )         
        serializer = ProfesionalSerializer(modelo_vista)
        return Response (serializer.data, status=status.HTTP_200_OK)