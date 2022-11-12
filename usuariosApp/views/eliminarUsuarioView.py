from rest_framework.response import Response
from rest_framework import generics, status, authentication
from rest_framework.permissions import IsAuthenticated

from usuariosApp.models.usuario import Usuario
from usuariosApp.serializers.usuarioSerializer import UsuarioSerializer

class EliminarUsuarioView(generics.RetrieveAPIView):
    authentication_classes = [authentication.TokenAuthentication]

    def get_object(self, id):
        try:
            return Usuario.objects.get(id=id)
        except Usuario.DoesNotExist:
            return None

    def delete(self, request, *args, **kwargs ):
        usuario_instance = self.get_object(kwargs['pk'])
        if not usuario_instance:
            return Response(
                {"res":"El usuario asignado con este id no existe"},
                status=status.HTTP_400_BAD_REQUEST
            )
        usuario_instance.delete()
        return Response(
            {"res":"El usuario asignado con este id fue eliminado con exito"},
            status=status.HTTP_200_OK   
        )