import json
import socket
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message, Conversation
from django.contrib.auth.models import User

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.conversation_id = self.scope['url_route']['kwargs']['conversation_id']
        self.room_group_name = f'chat_{self.conversation_id}'

        # Ajouter le client au groupe de la conversation
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Retirer le client du groupe de la conversation
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        sender_id = data['sender_id']
        receiver_id = data['receiver_id']

        # Enregistrer le message dans la base de données
        sender = User.objects.get(id=sender_id)
        receiver = User.objects.get(id=receiver_id)
        conversation = Conversation.objects.get(id=self.conversation_id)
        Message.objects.create(
            conversation=conversation,
            sender=sender,
            receiver=receiver,
            content=message
        )

        # Envoyer le message à tous les clients connectés au groupe
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': sender.username,
                'receiver': receiver.username
            }
        )

    async def chat_message(self, event):
        # Envoyer le message au WebSocket client
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'sender': event['sender'],
            'receiver': event['receiver']
        }))