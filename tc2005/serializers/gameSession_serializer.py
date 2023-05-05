from rest_framework import serializers

from tc2005.models import GameSession





class GameSessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = GameSession
        fields = "__all__"

class playerSerializer(serializers.Serializer):

    id = serializers.CharField(

        required=True,
        
    )

class GameSerializer(serializers.Serializer):

    playerId = serializers.CharField(

        required=True,
        
    )
    modulo = serializers.CharField(

        required=True,
    
        
    )

    nivel = serializers.CharField(
        required=True
    )

    velocidad = serializers.CharField(
        required=True
    )
    errores = serializers.CharField(
        required=True
    )