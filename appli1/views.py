from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Cricketteam
from .serializers import CricketteamSerializers
# Create your views here.

@api_view(['GET'])
def details(request):
    team = Cricketteam.objects.all()
    serializer = CricketteamSerializers(team, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create(request):
    serializer = CricketteamSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print('save')
    return Response(serializer.data)
       
@api_view(['DELETE'])
def delete(request,pk):
    team = Cricketteam.objects.get(id=pk)
    team.delete()
    return Response("Deleted Sucessfully")

@api_view(['PUT'])
def update(request, pk):
    team = Cricketteam.objects.get(id=pk)
    serializer = CricketteamSerializers(instance=team, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    