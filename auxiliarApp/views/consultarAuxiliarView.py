from rest_framework import generics, status, authentication
from rest_framework.response import Response

from auxiliarApp.models.auxiliar import Auxiliar
from auxiliarApp.serializers.auxiliarSerializer import AuxiliarSerializer

class ConsultarAuxiliarView(generics.RetrieveAPIView):
    authentication_classes = [authentication.TokenAuthentication]

    def get(self, request, *args, **kwargs):
        modelo_vista = Auxiliar.objects.get(id_usuario=kwargs['pk'])
        serializer = AuxiliarSerializer(modelo_vista)
        return Response (serializer.data, status=status.HTTP_200_OK)