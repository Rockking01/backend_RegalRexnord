from rest_framework import viewsets
from tc2005.models import AuthRegistro
from tc2005.serializers.AuthRegistro_serializer import AuthRegistroSerializer, tokenSerializer
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
        
    @action(methods=["POST"],  detail=False, serializer_class=tokenSerializer, permission_classes=[IsAuthenticated])
    def authenticateToken(self, request):
        serializer = tokenSerializer(data=request.data)
        if serializer.is_valid():
            auth_key = serializer.validated_data["token"]

            try:
                auth_registro = AuthRegistro.objects.get(authKey=auth_key, status=AuthRegistro.ACTIVE)
                
                return Response({"status": "Token is valid"})
            except AuthRegistro.DoesNotExist:
                return Response({"error": "Invalid or inactive token"}, status=status.HTTP_400_BAD_REQUEST)

        
    @action(methods=["PUT"],  detail=False, serializer_class=AuthRegistroSerializer, permission_classes=[IsAuthenticated])
    def updateToken(self, request):
        serializer = tokenSerializer(data=request.data)
        if serializer.is_valid():
            auth_key = serializer.validated_data["token"]

            try:
                auth_reg = AuthRegistro.objects.get(authKey=auth_key, status=AuthRegistro.ACTIVE)
                auth_reg.status = AuthRegistro.USED
                auth_reg.save()
                return Response({"status": "Token has been used"})
            except AuthRegistro.DoesNotExist:
                return Response({"error": "Invalid or inactive token"}, status=status.HTTP_400_BAD_REQUEST)