from rest_framework.response import Response
from rest_framework import generics, status, authentication
from rest_framework.permissions import IsAuthenticated

from signosVitalesApp.models import SignosVitales
from signosVitalesApp.serializers import SignosVitalesSerializer

class ConsultarSignosVitalesPorPaciente(generics.RetrieveAPIView):
    authentication_classes = [authentication.TokenAuthentication]

    def get(self, request, *args, **kwargs):
        try:
            modelo_vista = SignosVitales.objects.filter(id_paciente=kwargs['pk'])
        except SignosVitales.DoesNotExist:
            return Response(
                {'Los signos vitales asignados con este id no existen'},
                status = status.HTTP_400_BAD_REQUEST
            )
        serializer = SignosVitalesSerializer(modelo_vista, many= True)
        return Response (serializer.data, status=status.HTTP_200_OK)