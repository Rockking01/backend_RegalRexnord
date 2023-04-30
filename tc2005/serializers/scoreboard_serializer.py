from rest_framework import serializers
from tc2005.models import Scoreboard
from .user_serializer import UserSerializer




class ScoreboardSerializer(serializers.ModelSerializer):

   
    class Meta:
        model = Scoreboard
        fields = "__all__"
    
class ScoreSerializer(serializers.Serializer):
    score = serializers.IntegerField( required=True)