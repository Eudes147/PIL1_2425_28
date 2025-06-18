from rest_framework import serializers
from .models import Message, Conversation

class ConversationSerializer(serializers.ModelSerializer):
    participants = serializers.StringRelatedField(many=True)

    class Meta:
        model = Conversation
        fields = ['id', 'participants', 'created_at']

class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.StringRelatedField()
    receiver = serializers.StringRelatedField()

    class Meta:
        model = Message
        fields = ['id', 'conversation', 'sender', 'receiver', 'content', 'timestamp']