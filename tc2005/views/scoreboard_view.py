from rest_framework import viewsets
from tc2005.models import Scoreboard
from tc2005.serializers.scoreboard_serializer import ScoreboardSerializer, ScoreSerializer
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import  status

from ..models import User

class ScoreboardView(viewsets.ModelViewSet):
    queryset = Scoreboard.objects.all() # Select * from user;
    serializer_class = ScoreboardSerializer
    authentication_classes = (SessionAuthentication, TokenAuthentication, )

    @action(methods=["POST"],  detail=False, serializer_class=ScoreSerializer, permission_classes=[IsAuthenticated])
    def register_score(self, request):

        serializer = ScoreSerializer(data=request.data)

        if serializer.is_valid():
            user = User.objects.get(email=request.user)
            score = Scoreboard.objects.create(
                user=user,
                score=serializer.validated_data["score"]
            )
            score.save()
        
            return Response({"detail": "Score saved"}, status=status.HTTP_200_OK) 
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)