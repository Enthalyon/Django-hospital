from rest_framework.response import Response
from rest_framework import generics, status, authentication

from signosVitalesApp.models import SignosVitales
from signosVitalesApp.serializers import SignosVitalesSerializer

class ActualizarSignosVitalesView(generics.RetrieveAPIView):
    authentication_classes = [authentication.TokenAuthentication]

    def get_object(self, id):
        try:
            return SignosVitales.objects.get(id=id)
        except SignosVitales.DoesNotExist:
            return None
            
    def put (self, request, *args, **kwargs):
        signos_instance = self.get_object(kwargs['pk'])
        if not signos_instance:
            return Response(
                {'Los signos vitales asignados con este id no existen.'},
                status = status.HTTP_400_BAD_REQUEST
            )
        serializer = SignosVitalesSerializer(instance= signos_instance, data= request.data, partial= True)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
