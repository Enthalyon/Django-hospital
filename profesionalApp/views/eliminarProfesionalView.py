from rest_framework.response import Response
from rest_framework import generics, status, authentication

from profesionalApp.models import ProfesionalMedico
from profesionalApp.serializers import ProfesionalSerializer


class EliminarProfesionalView(generics.RetrieveAPIView):
    authentication_classes = [authentication.TokenAuthentication]

    def get_object(self, id):
        try:
            return ProfesionalMedico.objects.get(id=id)
        except ProfesionalMedico.DoesNotExist:
            return None

    def delete(self, request, *args, **kwargs ):
        profesional_instance = self.get_object(kwargs['pk'])
        if not profesional_instance:
            return Response(
                {"res":"El profesional asignado con este id no existe"},
                status=status.HTTP_400_BAD_REQUEST
            )
        profesional_instance.delete()
        return Response(
            {"res":"El profesional asignado con este id fue eliminado con exito"},
            status=status.HTTP_200_OK   
        )