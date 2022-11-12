from rest_framework.response import Response
from rest_framework import generics, status, authentication
from rest_framework.permissions import IsAuthenticated

from signosVitalesApp.models import SignosVitales
from signosVitalesApp.serializers import SignosVitalesSerializer

class CrearSignosVitalesView(generics.RetrieveAPIView):
    authentication_classes = [authentication.TokenAuthentication]

    def post(self, request, *args, **kwargs):
        serializer = SignosVitalesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)