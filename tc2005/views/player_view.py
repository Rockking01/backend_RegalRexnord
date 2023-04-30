from rest_framework import viewsets
from tc2005.models import Player
from tc2005.serializers.player_serializer import PlayerSerializer
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import  status

from ..models import User

class PlayerView(viewsets.ModelViewSet):
    queryset = Player.objects.all() # Select * from user;
    serializer_class = PlayerSerializer
    authentication_classes = (SessionAuthentication, TokenAuthentication, )

    @action(methods=["POST"],  detail=False, serializer_class=PlayerSerializer, permission_classes=[IsAuthenticated])
    def register_player(self, request):

        serializer = PlayerSerializer(data=request.data)

        if serializer.is_valid():
            user = User.objects.get(email=request.user)
            aggregateScore = Player.objects.create(
                user=user,
                aggregateScore=serializer.validated_data["aggregateScore"]
            )
            aggregateScore.save()
        
            return Response({"detail": "player saved"}, status=status.HTTP_200_OK) 
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)