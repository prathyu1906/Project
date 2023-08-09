from rest_framework import serializers
from .models import Cricketteam

class CricketteamSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cricketteam
        fields = ['id','name','player_no','age','total_runs']
        