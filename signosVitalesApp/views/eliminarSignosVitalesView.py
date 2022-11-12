from rest_framework.response import Response
from rest_framework import generics, status, authentication

from signosVitalesApp.models import SignosVitales
from signosVitalesApp.serializers import SignosVitalesSerializer

class EliminarSignosVitalesView(generics.RetrieveAPIView):
    authentication_classes = [authentication.TokenAuthentication]

    def get_object(self, id):
        try:
            return SignosVitales.objects.get(id=id)
        except SignosVitales.DoesNotExist:
            return None

    def delete(self, request, *args, **kwargs ):
        signos_instance = self.get_object(kwargs['pk'])
        if not signos_instance:
            return Response(
                {"res":"Los signos vitales asignados con este id no existen"},
                status=status.HTTP_400_BAD_REQUEST
            )
        signos_instance.delete()
        return Response(
            {"res":"Los signos vitales asignados con este id fueron eliminados con exito"},
            status=status.HTTP_200_OK   
        )