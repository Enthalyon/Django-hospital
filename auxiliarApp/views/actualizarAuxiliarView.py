from rest_framework.response import Response
from rest_framework import generics, status, authentication

from auxiliarApp.models.auxiliar import Auxiliar
from auxiliarApp.serializers.auxiliarSerializer import AuxiliarSerializer

class ActualizarAuxiliarView(generics.RetrieveAPIView):
    authentication_classes = [authentication.TokenAuthentication]

    def get_object(self, id):
        try:
            return Auxiliar.objects.get(id=id)
        except Auxiliar.DoesNotExist:
            return None

    def put (self, request, *args, **kwargs):
        auxiliar_instance = self.get_object(kwargs['pk'])
        if not auxiliar_instance:
            return Response(
                {'El auxiliar asignado con este id no existe.'},
                status = status.HTTP_400_BAD_REQUEST
            )
        serializer = AuxiliarSerializer(instance= auxiliar_instance, data= request.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
