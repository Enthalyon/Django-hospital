from django.conf import settings
from rest_framework import generics, status, views, authentication
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from usuariosApp.models.usuario import Usuario
from usuariosApp.serializers.usuarioSerializer import UsuarioSerializer

class ConsultaUsuarioPorToken(views.APIView):
    authentication_classes = [authentication.TokenAuthentication]

    def get_object(self, id):
      try:
        return Usuario.objects.get(id=id)
      except Usuario.DoesNotExist:
        return None

    def get(self, request, *args, **kwargs):
        bearer = request.META.get('HTTP_AUTHORIZATION');
        if(bearer == None or bearer == ""):
          stringResponse = {'detail':'Necesitas estar autentificado'}
          return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        token = bearer[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)
        
        usuario = self.get_object(valid_data['user_id'])
        if not usuario:
          Response({'detail': "Usuario inexistente"}, status=status.HTTP_404_NOT_FOUND)
        serializer = UsuarioSerializer(usuario)
        return Response(
            {
              "id": serializer.data['id'],
              "email": serializer.data['email']       
            }, 
            status=status.HTTP_200_OK
          )