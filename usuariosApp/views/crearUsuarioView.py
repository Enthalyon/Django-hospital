from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from usuariosApp.serializers.usuarioSerializer import UsuarioSerializer

class CrearUsuarioView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = UsuarioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        tokenData = {"email":request.data["email"],
                    "password":request.data["password"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)

        return Response(
            {
              "id": serializer.data['id'],
              "refresh": tokenSerializer.validated_data['refresh'],
              "access": tokenSerializer.validated_data['access']
            }, 
            status=status.HTTP_201_CREATED
          )