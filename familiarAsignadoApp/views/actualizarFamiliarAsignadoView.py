from rest_framework.response import Response
from rest_framework import generics, status, authentication

from familiarAsignadoApp.models import FamiliarAsignado
from familiarAsignadoApp.serializers import FamiliarAsignadoSerializer

class ActualizarFamiliarAsignadoView(generics.RetrieveAPIView):
    authentication_classes = [authentication.TokenAuthentication]

    def get_object(self, id):
        try:
            return FamiliarAsignado.objects.get(id=id)
        except FamiliarAsignado.DoesNotExist:
            return None
            
    def put (self, request, *args, **kwargs):
        familiar_instance = self.get_object(kwargs['pk'])
        if not familiar_instance:
            return Response(
                {'El familiar asignado con este id no existe.'},
                status = status.HTTP_400_BAD_REQUEST
            )
        serializer = FamiliarAsignadoSerializer(instance= familiar_instance, data= request.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
