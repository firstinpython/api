from django.shortcuts import render
from rest_framework import generics
from .models import Videos
from .serializers import VideosSerializers
# Create your views here.

class VideoList(generics.ListAPIView):
    queryset = Videos.objects.all()
    serializer_class = VideosSerializers



class VideoCreate(generics.CreateAPIView):
    queryset = Videos.objects.all()
    serializer_class = VideosSerializers

