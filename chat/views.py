from django.shortcuts import render
from rest_framework import generics, permissions 
from rest_framework.response import responses
from rest_framework.views import APIView
from .models import Message
from .serializers import MessageSerializer
from django.db.models import Q
from django.contrib.auth.models import User
# Create your views here.

class MessageListCreateAPIViews(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        User = self.request.user
        targuet_user_id = self.request.query_params.get('user_id')
        if targuet_user_id :
            try :
                targuet_user = User.objects.get(id=targuet_user_id)
                queryset = Message.objects.filter((Q(sender = User)& Q(receiver = User)) |
                 (Q(senser = targuet_user)& Q(receiver = User))                                 ).order_by('timestamp')
            except User.DoesNotExist:
                queryset = Message.objects.none()
        else:
            queryset = Message.objects.filter(Q(senser = User) | Q(receicer = User)).order_by('timestamp')
        return queryset
    def perform_create(self, serializer):
        serializer.save(sender = self.request.user)