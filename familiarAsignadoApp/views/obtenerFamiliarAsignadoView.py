from rest_framework.response import Response
from rest_framework import generics, status, authentication

from familiarAsignadoApp.models import FamiliarAsignado
from familiarAsignadoApp.serializers import FamiliarAsignadoSerializer

class ObtenerFamiliarAsignadoView(generics.RetrieveAPIView):
    authentication_classes = [authentication.TokenAuthentication]

    def get(self, request, *args, **kwargs):
        modelo_vista = FamiliarAsignado.objects.get(id=kwargs['pk'])
        if not modelo_vista:
            return Response(
                {"res":"El familiar con este id no existen"},
                status=status.HTTP_400_BAD_REQUEST
            )         
        serializer = FamiliarAsignadoSerializer(modelo_vista)
        return Response (serializer.data, status=status.HTTP_200_OK)