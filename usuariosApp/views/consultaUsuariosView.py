from django.conf import settings
from rest_framework import generics, status, authentication, views
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from usuariosApp.models.usuario import Usuario
from usuariosApp.serializers.usuariosSerializer import UsuariosSerializer

class ConsultaUsuariosView(views.APIView):
    queryset = Usuario.objects.all()
    authentication_classes = [authentication.TokenAuthentication]

    def get_object(self):
        try:
            return Usuario.objects.all()
        except Usuario.DoesNotExist:
            return None

    def get(self, request, *args, **kwargs):
        bearer = request.META.get('HTTP_AUTHORIZATION');
        if(bearer == None or bearer == ""):
            stringResponse = {'detail':'Necesitas estar autentificado'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        usuarios = self.get_object()
        print(usuarios)
        if not usuarios:
            Response({'detail': "Usuarios inexistentes"}, status=status.HTTP_404_NOT_FOUND)
        serializer = UsuariosSerializer(usuarios, many = True)
        return Response(
                serializer.data, 
            status=status.HTTP_200_OK
            )