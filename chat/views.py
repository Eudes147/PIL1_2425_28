from rest_framework import generics
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer

class ConversationListView(generics.ListAPIView):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filtrer les conversations pour inclure uniquement celles où l'utilisateur est un participant
        return Conversation.objects.filter(participants=self.request.user)

class ConversationDetailView(generics.RetrieveAPIView):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated]

class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Associer l'expéditeur au message
        serializer.save(sender=self.request.user)
        
        
        
def chat_view(request):
    return render(request, 'chat/chat.html')

def conversation(request):
    return render(request, 'chat/conversation.html')    