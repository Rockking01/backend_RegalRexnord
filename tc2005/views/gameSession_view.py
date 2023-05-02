from rest_framework import viewsets
from tc2005.models import GameSession
from tc2005.serializers.gameSession_serializer import GameSessionSerializer, playerSerializer
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.serializers import ValidationError
from rest_framework import  status

from ..models import User

class GameSessionView(viewsets.ModelViewSet):
    queryset = GameSession.objects.all() # Select * from user;
    serializer_class = GameSessionSerializer
    authentication_classes = (SessionAuthentication, TokenAuthentication, )

    @action(methods=["POST"],  detail=False, serializer_class=GameSessionSerializer, permission_classes=[AllowAny])
    def register_gameSession(self, request):

        serializer = GameSessionSerializer(data=request.data)

        if serializer.is_valid():
            player = User.objects.get(email=request.user)
            session = GameSession.objects.create(
                player=player,
                session=serializer.validated_data["session"]
            )
            session.save()
        
            return Response({"detail": "session saved"}, status=status.HTTP_200_OK) 
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    @action(methods=["POST"],  detail=False, serializer_class=playerSerializer, permission_classes=[AllowAny])
    def specificUser(self,request):
    
        serializer = playerSerializer(data=request.data)

        if serializer.is_valid(): 
            id = serializer.validated_data["id"]
            

            try:
                sessions = GameSession.objects.filter(playerid=id)
                gameserializer = GameSessionSerializer(sessions, many=True)
            
            except BaseException as e:
                raise ValidationError({"error": str(e)})
            

            return Response({"sessiones": gameserializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
    @action(methods=["GET"],  detail=False, serializer_class=GameSessionSerializer, permission_classes=[AllowAny])
    def get_gameSession(self, request):
        game_sessions = GameSession.objects.all()
        serializer = self.get_serializer(game_sessions, many=True)
        return Response(serializer.data)
    

    

                
      

    