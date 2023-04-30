from rest_framework import viewsets
from tc2005.models import GameSession
from tc2005.serializers.gameSession_serializer import GameSessionSerializer
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import  status

from ..models import Player

class GameSessionView(viewsets.ModelViewSet):
    queryset = GameSession.objects.all() # Select * from user;
    serializer_class = GameSessionSerializer
    authentication_classes = (SessionAuthentication, TokenAuthentication, )

    @action(methods=["POST"],  detail=False, serializer_class=GameSessionSerializer, permission_classes=[IsAuthenticated])
    def register_gameSession(self, request):

        serializer = GameSessionSerializer(data=request.data)

        if serializer.is_valid():
            player = Player.objects.get(email=request.player)
            session = GameSession.objects.create(
                player=player,
                session=serializer.validated_data["session"]
            )
            session.save()
        
            return Response({"detail": "session saved"}, status=status.HTTP_200_OK) 
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)