from django.shortcuts import render

# Create your views here.
from .models import Travel
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import TravelSerializer

class TravelViewSet(viewsets.ModelViewSet):

    ## The Main Query for the index route
    queryset = Travel.objects.all()

    # The serializer class for serializing output
    serializer_class = TravelSerializer

    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]