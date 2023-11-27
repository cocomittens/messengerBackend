from django.shortcuts import render
from rest_framework import viewsets
from .models import Message, UserProfile
from .serializers import MessageSerializer, UserProfileSerializer

# Create your views here.
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('-date')
    serializer_class = MessageSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer