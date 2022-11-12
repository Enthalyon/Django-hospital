from rest_framework import generics, status, authentication
from rest_framework.response import Response

from auxiliarApp.models.auxiliar import Auxiliar
from auxiliarApp.serializers.auxiliarSerializer import AuxiliarSerializer

class CrearAuxiliarView(generics.RetrieveAPIView):
    authentication_classes = [authentication.TokenAuthentication]

    def post(self, request, *args, **kwargs):
        serializer = AuxiliarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)