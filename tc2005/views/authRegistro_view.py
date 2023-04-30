from rest_framework import viewsets
from tc2005.models import AuthRegistro
from tc2005.serializers.AuthRegistro_serializer import AuthRegistroSerializer
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import  status



class AuthRegistroView(viewsets.ModelViewSet):
    queryset = AuthRegistro.objects.all() # Select * from user;
    serializer_class = AuthRegistroSerializer
    authentication_classes = (SessionAuthentication, TokenAuthentication, )

    @action(methods=["POST"],  detail=False, serializer_class=AuthRegistroSerializer, permission_classes=[IsAuthenticated])
    def register_authregistro(self, request):

        serializer = AuthRegistroSerializer(data=request.data)

        if serializer.is_valid():
            authregistro = AuthRegistro.objects.create(
                
                authregistro=serializer.validated_data["authregistro"]
            )
            authregistro.save()
        
            return Response({"detail": "auth saved"}, status=status.HTTP_200_OK) 
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)