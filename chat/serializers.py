from rest_framework import serializers
from .models import Message, UserProfile

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'sender', 'recipient', 'message', 'date')

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'image', 'online')