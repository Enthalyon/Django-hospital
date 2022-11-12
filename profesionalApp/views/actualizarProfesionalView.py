from rest_framework.response import Response
from rest_framework import generics, status, authentication

from profesionalApp.models import ProfesionalMedico
from profesionalApp.serializers import ProfesionalSerializer

class ActualizarProfesionalView(generics.RetrieveAPIView):
    authentication_classes = [authentication.TokenAuthentication]

    def get_object(self, id):
        try:
            return ProfesionalMedico.objects.get(id=id)
        except ProfesionalMedico.DoesNotExist:
            return None
            
    def put (self, request, *args, **kwargs):
        profesional_instance = self.get_object(kwargs['pk'])
        if not profesional_instance:
            return Response(
                {'El profesional asignado con este id no existe.'},
                status = status.HTTP_400_BAD_REQUEST
            )
        serializer = ProfesionalSerializer(instance= profesional_instance, data= request.data, partial= True)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
