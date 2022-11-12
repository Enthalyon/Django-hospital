from rest_framework.response import Response
from rest_framework import generics, status, authentication

from profesionalApp.models import ProfesionalMedico
from profesionalApp.serializers import ProfesionalSerializer

class CrearProfesionalView(generics.RetrieveAPIView):
    authentication_classes = [authentication.TokenAuthentication]

    def post(self, request, *args, **kwargs):
        serializer = ProfesionalSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)