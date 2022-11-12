from rest_framework.response import Response
from rest_framework import generics, status, views, authentication
#from rest_framework.permissions import IsAuthenticated

from usuariosApp.models.usuario import Usuario
from usuariosApp.serializers.usuarioSerializer import UsuarioSerializer

class ActualizarUsuarioView(views.APIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    authentication_classes = [authentication.TokenAuthentication]

    def get_object(self, id):
        try:
            return Usuario.objects.get(id=id)
        except Usuario.DoesNotExist:
            return None
            
    def put (self, request, *args, **kwargs):
        usuario_instance = self.get_object(kwargs['pk'])
        if not usuario_instance:
            return Response(
                {'El usuario asignado con este id no existe'},
                status = status.HTTP_400_BAD_REQUEST
            )
        serializer = UsuarioSerializer(instance= usuario_instance, data= request.data, partial= True)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
