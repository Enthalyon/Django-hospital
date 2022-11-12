from rest_framework.response import Response
from rest_framework import generics, status, authentication

from familiarAsignadoApp.models import FamiliarAsignado
from familiarAsignadoApp.serializers import FamiliarAsignadoSerializer

class EliminarFamiliarAsignadoView(generics.RetrieveAPIView):
    authentication_classes = [authentication.TokenAuthentication]

    def get_object(self, id):
        try:
            return FamiliarAsignado.objects.get(id=id)
        except FamiliarAsignado.DoesNotExist:
            return None

    def delete(self, request, *args, **kwargs ):
        familiar_instance = self.get_object(kwargs['pk'])
        if not familiar_instance:
            return Response(
                {"res":"El familiar asignado con este id no existe"},
                status=status.HTTP_400_BAD_REQUEST
            )
        familiar_instance.delete()
        return Response(
            {"res":"El familiar asignado fue eliminado con exito"},
            status=status.HTTP_200_OK   
        )