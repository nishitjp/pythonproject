from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .models import Songs
from .serializers import SongsSerializer

class songlist(viewsets.ModelViewSet):
    queryset=Songs.objects.all()
    serializer_class=SongsSerializer






 