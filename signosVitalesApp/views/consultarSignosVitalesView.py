from rest_framework.response import Response
from rest_framework import generics, status, authentication

from signosVitalesApp.models import SignosVitales
from signosVitalesApp.serializers import SignosVitalesSerializer

class ConsultarSignosVitalesView(generics.RetrieveAPIView):
    authentication_classes = [authentication.TokenAuthentication]

    def get(self, request, *args, **kwargs):
        modelo_vista = SignosVitales.objects.get(id=kwargs['pk'])
        if not modelo_vista:
            return Response(
                {"res":"Los signos vitales asignados con este id no existen"},
                status=status.HTTP_400_BAD_REQUEST
            )        
        serializer = SignosVitalesSerializer(modelo_vista)
        return Response (serializer.data, status=status.HTTP_200_OK)