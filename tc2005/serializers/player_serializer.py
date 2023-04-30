from rest_framework import serializers
from tc2005.models import Player





class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = "__all__"
    
