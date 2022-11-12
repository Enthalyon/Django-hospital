from rest_framework.response import Response
from rest_framework import generics, status, authentication

from familiarAsignadoApp.models import FamiliarAsignado
from familiarAsignadoApp.serializers import FamiliarAsignadoSerializer

class CrearFamiliarAsignadoView(generics.RetrieveAPIView):
    authentication_classes = [authentication.TokenAuthentication]

    def post(self, request, *args, **kwargs):
        serializer = FamiliarAsignadoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)