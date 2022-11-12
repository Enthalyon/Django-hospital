from rest_framework import generics, status, authentication
from rest_framework.response import Response

from auxiliarApp.models.auxiliar import Auxiliar
from auxiliarApp.serializers.auxiliarSerializer import AuxiliarSerializer

class EliminarAuxiliarView(generics.RetrieveAPIView):
    authentication_classes = [authentication.TokenAuthentication]

    def get_object(self, id):
        try:
            return Auxiliar.objects.get(id=id)
        except Auxiliar.DoesNotExist:
            return None

    def delete(self, request, *args, **kwargs ):
        auxiliar_instance = self.get_object(kwargs['pk'])
        if not auxiliar_instance:
            return Response(
                {"res":"El auxiliar asignado con este id no existe"},
                status=status.HTTP_400_BAD_REQUEST
            )
        auxiliar_instance.delete()
        return Response(
            {"res":"El auxiliar asignado fue eliminado con exito"},
            status=status.HTTP_200_OK   
        )